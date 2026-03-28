#!/usr/bin/env python3
"""
honors_event_stats_safe.py
-----------------------------
Processes Honors College event data safely.
Handles encoding issues, missing columns, cleans names, calculates
cohort-normalized metrics, categorizes event size, applies SPICES classification,
and outputs pivot tables and summary stats.
"""

import pandas as pd
import sys

# ---------- CONFIG ----------
RAW_CSV_PATHS = [
    "data/raw/Honors College Event Data 24-25(Fall 2024)(1).csv",
    "data/events.csv"
]

PROCESSED_CSV_PATH = "data/processed/honors_events_science_processed.csv"
HC_COHORT_SIZE = 460  # adjust per semester

# ---------- LOAD DATA WITH ENCODING FALLBACK ----------
df = None
for path in RAW_CSV_PATHS:
    for enc in ["utf-8", "latin1", "cp1252"]:
        try:
            df = pd.read_csv(path, encoding=enc)
            print(f"✅ Loaded '{path}' successfully with encoding: {enc}")
            break
        except Exception as e:
            print(f"❌ Failed to load '{path}' with encoding {enc}: {e}")
    if df is not None:
        break

if df is None:
    print("❌ Could not load any CSV. Exiting.")
    sys.exit(1)

# ---------- CLEAN COLUMN NAMES ----------
df.columns = df.columns.str.strip()
print("\nColumns loaded:")
print(df.columns.tolist())

# ---------- OPTIONAL: Drop cancelled events if column exists ----------
if "Status" in df.columns:
    df = df[df["Status"] != "Cancelled"].copy()
else:
    print("⚠️ 'Status' column not found; skipping cancelled events filter.")

# ---------- ENSURE NUMERIC COLUMNS ----------
numeric_cols = [
    '# Invited', '# RSVP Yes', '# RSVP No', '# RSVP Maybe',
    '# RSVP No Response', '# Marked Attended'
]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    else:
        print(f"⚠️ Column '{col}' not found; filling with zeros.")
        df[col] = 0

# ---------- COHORT-NORMALIZED METRICS ----------
df['Event_Size'] = df.get('# Marked Attended', 0)
df['Event_Size_%'] = df['Event_Size'] / HC_COHORT_SIZE * 100
df['Attendance_Rate'] = df['Event_Size'] / df.get('# RSVP Yes', 1).replace(0, 1)
df['Reach_Rate'] = df['Event_Size'] / df.get('# Invited', 1).replace(0, 1)
df['No_Response_%'] = df.get('# RSVP No Response', 0) / df.get('# Invited', 1).replace(0, 1)
df['Engagement_Index'] = (
    0.5 * df['Reach_Rate'] +
    0.3 * df['Attendance_Rate'] +
    0.2 * (1 - df['No_Response_%'])
)

# ---------- COMMITTEE EVENT SIZE BUCKETS ----------
def size_category(x):
    if x <= 15:
        return "Small"
    elif x <= 34:
        return "Medium"
    else:
        return "Large"

df['Size_Category'] = df['Event_Size'].apply(size_category)

# ---------- SPICES CLASSIFICATION ----------
spices_keywords = {
    "Service": ["volunteer", "community", "service"],
    "Professional Development": ["professional", "networking", "career", "scholarship", "info session"],
    "Intellectual Achievement": ["research", "academic", "study abroad", "competition", "thesis"],
    "Cultural Exploration": ["cultural", "museum", "arts", "performance", "exploration", "citymester"],
    "Engaged Living": ["social", "dinner", "lunch", "tailgate", "snacks", "meet & greet"],
    "Skill Development": ["workshop", "training", "resume", "planning", "writing", "strategy", "panel"]
}

def classify_spices(title, description):
    text = f"{title} {description}".lower()
    for category, keywords in spices_keywords.items():
        if any(kw.lower() in text for kw in keywords):
            return category
    return "Other"

df['SPICES Category'] = df.apply(
    lambda row: classify_spices(row.get('Event Title', ''), str(row.get('Description', ''))),
    axis=1
)

# ---------- PIVOT TABLES ----------
pivot_count = df.pivot_table(
    index='SPICES Category',
    columns='Size_Category',
    values='Event_Size',
    aggfunc='count',
    fill_value=0
)

pivot_avg_engagement = df.pivot_table(
    index='SPICES Category',
    columns='Size_Category',
    values='Engagement_Index',
    aggfunc='mean'
)

# ---------- SUMMARY STATS ----------
summary_cols = ['Event_Size_%', 'Attendance_Rate', 'Reach_Rate', 'No_Response_%', 'Engagement_Index']
summary_stats = df[summary_cols].describe().T

# ---------- OUTPUT ----------
print("\n--- SPICES Event Size Counts ---")
print(pivot_count)

print("\n--- SPICES Average Engagement Index ---")
print(pivot_avg_engagement.round(2))

print("\n--- Summary Statistics ---")
print(summary_stats.round(3))

# ---------- SAVE CSV ----------
df.to_csv(PROCESSED_CSV_PATH, index=False)
print(f"\n✅ Processed CSV saved to {PROCESSED_CSV_PATH}")
