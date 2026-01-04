import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


# --------------------------------------------------
# Configuration
# --------------------------------------------------
CSV_PATH = "data/processed/honors_events_science_processed.csv"
TARGET_COL = "# Marked Attended"


# --------------------------------------------------
# Load and prepare data
# --------------------------------------------------
def load_data(path):
    df = pd.read_csv(path)

    # Drop rows with no attendance info
    df = df.dropna(subset=[TARGET_COL])

    # Create binary target: high vs low attendance
    median_attendance = df[TARGET_COL].median()
    df["high_attendance"] = (df[TARGET_COL] > median_attendance).astype(int)

    # Basic time features
    df["Start Date"] = pd.to_datetime(df["Start Date"], errors="coerce")
    df["day_of_week"] = df["Start Date"].dt.dayofweek

    df["Start Time"] = pd.to_datetime(df["Start Time"], errors="coerce")
    df["start_hour"] = df["Start Time"].dt.hour

    # Online vs in-person
    df["is_online"] = df["Online Location"].notna().astype(int)

    # Combine text fields
    df["text"] = (
        df["Event Title"].fillna("") + " " + df["Description"].fillna("")
    )

    return df


# --------------------------------------------------
# Build ML pipeline
# --------------------------------------------------
def build_pipeline():
    text_features = "text"
    categorical_features = ["Event Type", "Visibility"]
    numeric_features = ["start_hour", "day_of_week", "is_online"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("text", TfidfVectorizer(
                max_features=500,
                stop_words="english"
            ), text_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", "passthrough", numeric_features),
        ]
    )

    model = LogisticRegression(max_iter=1000)

    pipeline = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )

    return pipeline


# --------------------------------------------------
# Train, evaluate, explain
# --------------------------------------------------
def main():
    df = load_data(CSV_PATH)

    X = df[
        ["text", "Event Type", "Visibility", "start_hour", "day_of_week", "is_online"]
    ]
    y = df["high_attendance"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    # Evaluation
    y_pred = pipeline.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # --------------------------------------------------
    # Feature importance (explanation)
    # --------------------------------------------------
    model = pipeline.named_steps["model"]
    feature_names = pipeline.named_steps["preprocess"].get_feature_names_out()

    coefs = model.coef_[0]
    importance = pd.DataFrame(
        {"feature": feature_names, "weight": coefs}
    ).sort_values(by="weight", ascending=False)

    print("\nTop features increasing attendance likelihood:")
    print(importance.head(10))

    print("\nTop features decreasing attendance likelihood:")
    print(importance.tail(10))


if __name__ == "__main__":
    main()

