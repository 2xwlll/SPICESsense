# src/spicessense/semantic_match.py
"""
Semantic matcher using sentence-transformers.
This module encapsulates loading the model and computing similarity
between an event description and each SPICE concept.
"""

import numpy as np

try:
    from sentence_transformers import SentenceTransformer, util
    SENT_TRANSFORMERS_AVAILABLE = True
except Exception:
    SENT_TRANSFORMERS_AVAILABLE = False

class SemanticMatcher:
    """
    Wraps a SentenceTransformer model to compute a similarity score for each SPICE.
    If sentence-transformers is unavailable, this class raises at init.
    """

    def __init__(self, spice_keyword_map, model_name="all-MiniLM-L6-v2"):
        if not SENT_TRANSFORMERS_AVAILABLE:
            raise RuntimeError("sentence-transformers not available. Install it to enable semantic matching.")
        self.model = SentenceTransformer(model_name)
        # Precompute embeddings for each SPICE aggregated keywords phrase
        self.spice_keys = list(spice_keyword_map.keys())
        # Join keywords into a phrase representing the SPICE to get a concept-level embedding
        self.spice_phrases = ["; ".join(spice_keyword_map[k]) for k in self.spice_keys]
        self.spice_embs = self.model.encode(self.spice_phrases, convert_to_numpy=True, show_progress_bar=False)
    
    def score(self, text):
        """
        Returns a dict {spice: similarity_score} (cosine in [-1,1]) for the input text.
        Higher means more semantically similar.
        """
        text_emb = self.model.encode([text], convert_to_numpy=True, show_progress_bar=False)[0]
        # cosine similarity between text_emb and spice_embs
        # cosine = (a·b) / (||a||*||b||)
        a = text_emb
        b = self.spice_embs  # shape (num_spices, dim)
        a_norm = np.linalg.norm(a) + 1e-12
        b_norm = np.linalg.norm(b, axis=1) + 1e-12
        sims = (b @ a) / (b_norm * a_norm)
        return {self.spice_keys[i]: float(sims[i]) for i in range(len(self.spice_keys))}

