# src/spicessense/keywords.py
"""
SPICES keyword dictionary for rule-based classification.
Keep this file small and editable — committee members can expand keywords over time.
"""

SPICES_KEYWORDS = {
    "Service": [
        "volunteer", "volunteering", "donation", "community", "service", "fundraiser",
        "outreach", "food drive", "service hours", "charity", "donate"
    ],
    "Professional Development": [
        "career", "resume", "cv", "interview", "network", "professional", "job fair",
        "internship", "employer", "mentorship", "leadership", "career services"
    ],
    "Intellectual Achievement Beyond the Classroom": [
        "research", "seminar", "academic", "paper", "poster", "conference", "presentation",
        "lecture", "symposium", "study", "colloquium", "workshop"  # note: workshop may map to skill too
    ],
    "Cultural Exploration": [
        "culture", "heritage", "festival", "diversity", "international", "tradition",
        "language", "global", "cultural", "ethnic"
    ],
    "Engaged Living": [
        "wellness", "health", "yoga", "mindfulness", "fitness", "self-care", "well-being",
        "meditation", "stress", "balance"
    ],
    "Skill Development": [
        "workshop", "training", "communication", "teamwork", "problem-solving",
        "public speaking", "presentation", "coding", "skill", "skills", "bootcamp"
    ],
}

