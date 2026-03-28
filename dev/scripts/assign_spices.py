import pandas as pd
import re

# -----------------------------
# Load data
# -----------------------------
CSV_PATH = "data/processed/honors_events_science_processed.csv"
OUTPUT_PATH = "data/processed/events_with_spices.csv"

df = pd.read_csv(CSV_PATH)

# Combine text fields
df["text"] = (
    df["Event Title"].fillna("") + " " +
    df["Description"].fillna("")
).str.lower()

# -----------------------------
# SPICES keyword dictionary
# -----------------------------
SPICES_KEYWORDS = {
    "Service": [
        "service", "volunteer", "community", "outreach", "nonprofit",
        "donation", "charity", "help", "support"
    ],
    "Professional Development": [
        "career", "resume", "cv", "internship", "professional",
        "linkedin", "networking", "interview", "job"
    ],
    "Intellectual Achievement": [
        "research", "lecture", "seminar", "colloquium",
        "presentation", "academic", "study", "scholar"
    ],
    "Cultural Exploration": [
        "culture", "cultural", "heritage", "diversity",
        "international", "global", "history", "tradition"
    ],
    "Engaged Living": [
        "wellness", "mental health", "fitness", "recreation",
        "community building", "belonging", "social", "mindfulness"
    ],
    "Skill Development": [
        "workshop", "training", "learn", "skills",
        "hands-on", "practice", "development"
    ]
}

# -----------------------------
# Tagging function
# -----------------------------
def assign_spices(text):
    labels = {}
    for category, keywords in SPICES_KEYWORDS.items():
        labels[category] = int(
            any(re.search(rf"\b{k}\b", text) for k in keywords)
        )
    return labels

# -----------------------------
# Apply tagging
# -----------------------------
spices_df = df["text"].apply(assign_spices).apply(pd.Series)

# Rename columns for clarity
spices_df.columns = [f"SPICES_{c.replace(' ', '_')}" for c in spices_df.columns]

# Merge back
df_out = pd.concat([df.drop(columns=["text"]), spices_df], axis=1)

# Save result
df_out.to_csv(OUTPUT_PATH, index=False)

print("SPICES tagging complete.")
print("Saved to:", OUTPUT_PATH)

