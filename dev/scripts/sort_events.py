import pandas as pd

# Load Excel file (replace with your file name)
df = pd.read_excel("honors_events.xlsx")

# Define SPICES categories and keyword triggers
spices_keywords = {
    "Service": [
        "volunteer", "service", "donation", "community", "outreach",
        "cleanup", "mentorship", "support"
    ],
    "Professional Development": [
        "career", "resume", "network", "internship", "professional",
        "job", "interview", "leadership", "fellow", "fellowship",
        "legislative", "citymester", "onca", "nsf", "scholarship",
        "graduate research", "application"
    ],
    "Intellectual Achievement beyond the classroom": [
        "research", "lecture", "academic", "panel", "discussion",
        "seminar", "presentation", "workshop", "symposium", "info session",
        "goldwater", "grfp", "academic achievement"
    ],
    "Cultural Exploration": [
        "culture", "cultural", "heritage", "festival", "music", "art",
        "film", "diversity", "tradition", "international", "exploration"
    ],
    "Engaged Living": [
        "social", "event", "tailgate", "hangout", "snack", "chat",
        "dinner", "celebration", "photo", "meet", "community", "fun"
    ],
    "Skill Development": [
        "skills", "training", "communication", "organization",
        "leadership", "writing", "learning", "practice", "growth"
    ]
}

# Assign SPICES category
def assign_spices(row):
    text = (
        str(row.get("Event Title", "")) + " " +
        str(row.get("Description", "")) + " " +
        str(row.get("Event Type", ""))
    ).lower()

    for category, keywords in spices_keywords.items():
        if any(keyword in text for keyword in keywords):
            return category

    return "Uncategorized"

# Apply the categorization
df["SPICES Category"] = df.apply(assign_spices, axis=1)

# Save the result
df.to_excel("honors_events_SPICES_labeled.xlsx", index=False)

print("✅ SPICES categories added successfully and saved to 'honors_events_SPICES_labeled.xlsx'")

