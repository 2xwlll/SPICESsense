# src/spicessense/classify.py
"""
Core classification logic for SPICESsense.
- Uses keyword matching first (deterministic, explainable).
- Falls back to semantic similarity if no keyword matches or for low-confidence cases.
"""

import re
from typing import List, Dict
import pandas as pd

from .keywords import SPICES_KEYWORDS

# Attempt to import semantic matcher, but handle absence gracefully
try:
    from .semantic_match import SemanticMatcher, SENT_TRANSFORMERS_AVAILABLE
    _SEM_AVAILABLE = SENT_TRANSFORMERS_AVAILABLE
except Exception:
    _SEM_AVAILABLE = False
    SemanticMatcher = None

# Precompile simple word boundary patterns to avoid substring false positives
def _word_in_text(word: str, text: str) -> bool:
    """
    Return True if 'word' appears as a term in text (case-insensitive),
    allowing simple phrases. Uses regex word boundaries for safety.
    """
    pattern = r"\b" + re.escape(word.lower()) + r"\b"
    return re.search(pattern, text.lower()) is not None

def assign_spices_keywords(text: str) -> List[str]:
    """
    Return list of SPICES that have at least one keyword present in text.
    """
    matches = []
    text_l = text.lower()
    for spice, keywords in SPICES_KEYWORDS.items():
        for kw in keywords:
            # check whole phrase or word match
            if _word_in_text(kw, text_l) or kw.lower() in text_l:
                matches.append(spice)
                break
    return matches

class SPICESClassifier:
    def __init__(self, use_semantic: bool = True, sem_threshold: float = 0.45):
        """
        use_semantic: attempt to use semantic fallback (requires sentence-transformers)
        sem_threshold: min cosine similarity to consider a SPICE relevant (0-1 typical)
        """
        self.use_semantic = use_semantic and _SEM_AVAILABLE
        self.sem_threshold = sem_threshold
        self.semantic = None
        if self.use_semantic:
            # Initialize semantic matcher with the SPICES keyword map
            self.semantic = SemanticMatcher(SPICES_KEYWORDS)
    
    def classify_text(self, title: str, description: str) -> Dict[str, float]:
        """
        Return dict {spice: score} where score is 1.0 for keyword matches, or semantic score for fallback.
        Keyword matches get priority and score=1.0
        """
        text = f"{title}. {description}"
        # 1) keyword matches
        kw_matches = assign_spices_keywords(text)
        scores = {}
        if kw_matches:
            # Give deterministic score 1.0 to keyword matches
            for s in kw_matches:
                scores[s] = 1.0
            # Optionally also compute semantic scores to surface additional suggestions
            if self.use_semantic:
                sem_scores = self.semantic.score(text)
                # add sem results above threshold but do not override keywords
                for spice, val in sem_scores.items():
                    if val >= self.sem_threshold and spice not in scores:
                        scores[spice] = float(val)  # lower-than-1 but meaningful
            return scores
        # 2) no keyword matches — try semantic (if available)
        if self.use_semantic:
            sem_scores = self.semantic.score(text)
            # return only those above threshold ordered by score
            filtered = {k: v for k, v in sem_scores.items() if v >= self.sem_threshold}
            # If nothing found above threshold, return top-2 as soft suggestions
            if not filtered:
                sorted_items = sorted(sem_scores.items(), key=lambda x: x[1], reverse=True)[:2]
                filtered = {k: float(v) for k, v in sorted_items}
            return filtered
        # 3) fallback: no semantic available — return 'Uncategorized'
        return {"Uncategorized": 0.0}
    
    def classify_dataframe(self, df: pd.DataFrame, title_col="Title", desc_col="Description") -> pd.DataFrame:
        """
        Apply classification to a dataframe with event rows. Returns a new DataFrame with a 'SPICES' column
        listing assigned SPICE(s) and 'SPICES_scores' for raw values.
        """
        rows = []
        for _, r in df.iterrows():
            title = str(r.get(title_col, "") or "")
            desc = str(r.get(desc_col, "") or "")
            result = self.classify_text(title, desc)
            # Sort by score descending, then format
            sorted_items = sorted(result.items(), key=lambda x: x[1], reverse=True)
            spices_list = [k for k, _ in sorted_items]
            scores_list = [v for _, v in sorted_items]
            rows.append({
                **r.to_dict(),
                "SPICES": "; ".join(spices_list),
                "SPICES_scores": "; ".join([f"{s:.3f}" for s in scores_list])
            })
        out_df = pd.DataFrame(rows)
        return out_df

