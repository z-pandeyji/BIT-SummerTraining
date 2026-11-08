from pathlib import Path

import os
import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ============================================================
# Responsible AI Audit
# Dataset: UCI Adult Income Dataset
# ============================================================

DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "adult/adult.data"
)

DATA_FILE = str(Path(__file__).with_name("adult.data"))

COLUMNS = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "income",
]


def load_dataset():
    """Download the public UCI Adult dataset if needed."""
    if not os.path.exists(DATA_FILE):
        print("Downloading UCI Adult dataset...")
        urllib.request.urlretrieve(DATA_URL, DATA_FILE)

    df = pd.read_csv(
        DATA_FILE,
        names=COLUMNS,
        skipinitialspace=True,
        na_values="?"
    )

    return df


def clean_dataset(df):
    """Remove missing rows and normalize labels."""
    df = df.copy()

    print("\nMissing values before cleaning:")
    print(df.isna().sum())

    df = df.dropna()

    df["income"] = (
        df["income"]
        .astype(str)
        .str.strip()
        .str.replace(".", "", regex=False)
    )

    df["sex"] = df["sex"].astype(str).str.strip()
    df["race"] = df["race"].astype(str).str.strip()

    return df


def fairness_audit(df):
    """Calculate demographic representation and income-rate differences."""

    print("\n" + "=" * 70)
    print("FAIRNESS AUDIT")
    print("=" * 70)

    # --------------------------------------------------------
    # Overall label distribution
    # --------------------------------------------------------

    income_distribution = (
        df["income"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    print("\nIncome label distribution (%):")
    print(income_distribution)

    # --------------------------------------------------------
    # Sex representation
    # --------------------------------------------------------

    sex_distribution = (
        df["sex"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    print("\nSex representation (%):")
    print(sex_distribution)

    # --------------------------------------------------------
    # Race representation
    # --------------------------------------------------------

    race_distribution = (
        df["race"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    print("\nRace representation (%):")
    print(race_distribution)

    # --------------------------------------------------------
    # Positive outcome rate by sex
    # --------------------------------------------------------

    sex_income_rate = (
        df.assign(high_income=df["income"] == ">50K")
        .groupby("sex")["high_income"]
        .mean()
        .mul(100)
        .round(2)
    )

    print("\nHigh-income outcome rate by sex (%):")
    print(sex_income_rate)

    # --------------------------------------------------------
    # Positive outcome rate by race
    # --------------------------------------------------------

    race_income_rate = (
        df.assign(high_income=df["income"] == ">50K")
        .groupby("race")["high_income"]
        .mean()
        .mul(100)
        .round(2)
    )

    print("\nHigh-income outcome rate by race (%):")
    print(race_income_rate)

    return sex_income_rate, race_income_rate


def build_model(df):
    """Train a simple baseline income classifier."""

    features = [
        "age",
        "education-num",
        "hours-per-week",
        "capital-gain",
        "capital-loss",
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    X = df[features]
    y = (df["income"] == ">50K").astype(int)

    categorical_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    numerical_features = [
        "age",
        "education-num",
        "hours-per-week",
        "capital-gain",
        "capital-loss",
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=True
                ),
                categorical_features,
            ),
            (
                "num",
                "passthrough",
                numerical_features,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight=None
                ),
            ),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)

    print("\n" + "=" * 70)
    print("OVERALL MODEL PERFORMANCE")
    print("=" * 70)

    print(f"Accuracy : {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall   : {recall:.3f}")

    # --------------------------------------------------------
    # Group performance by sex
    # --------------------------------------------------------

    test_data = X_test.copy()
    test_data["actual"] = y_test.values
    test_data["prediction"] = predictions

    group_results = []

    for group in sorted(test_data["sex"].unique()):
        subset = test_data[test_data["sex"] == group]

        group_accuracy = accuracy_score(
            subset["actual"],
            subset["prediction"]
        )

        group_recall = recall_score(
            subset["actual"],
            subset["prediction"],
            zero_division=0
        )

        group_positive_prediction_rate = (
            subset["prediction"].mean()
        )

        group_results.append(
            {
                "group": group,
                "samples": len(subset),
                "accuracy": round(group_accuracy, 4),
                "recall": round(group_recall, 4),
                "positive_prediction_rate": round(
                    group_positive_prediction_rate,
                    4
                ),
            }
        )

    group_df = pd.DataFrame(group_results)

    print("\nPerformance by sex:")
    print(group_df.to_string(index=False))

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "group_results": group_df,
    }


def create_visualizations(df, sex_income_rate, race_income_rate):
    """Create at least two audit visualizations."""

    # --------------------------------------------------------
    # Visualization 1: Income distribution
    # --------------------------------------------------------

    plt.figure(figsize=(7, 5))

    income_counts = df["income"].value_counts()

    plt.bar(
        income_counts.index,
        income_counts.values
    )

    plt.title("Income Label Distribution")
    plt.xlabel("Income Category")
    plt.ylabel("Number of Records")
    plt.tight_layout()

    plt.savefig(
        "audit_visualization_1.png",
        dpi=150
    )

    plt.close()

    # --------------------------------------------------------
    # Visualization 2: High-income rate by sex
    # --------------------------------------------------------

    plt.figure(figsize=(7, 5))

    plt.bar(
        sex_income_rate.index,
        sex_income_rate.values
    )

    plt.title("High-Income Outcome Rate by Sex")
    plt.xlabel("Sex")
    plt.ylabel("High-Income Rate (%)")
    plt.tight_layout()

    plt.savefig(
        "audit_visualization_2.png",
        dpi=150
    )

    plt.close()

    # --------------------------------------------------------
    # Visualization 3: High-income rate by race
    # --------------------------------------------------------

    plt.figure(figsize=(9, 5))

    plt.bar(
        race_income_rate.index,
        race_income_rate.values
    )

    plt.title("High-Income Outcome Rate by Race")
    plt.xlabel("Race")
    plt.ylabel("High-Income Rate (%)")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(
        "audit_visualization_3.png",
        dpi=150
    )

    plt.close()


def save_results(df, sex_income_rate, race_income_rate, model_results):
    """Save key audit measurements to CSV."""

    rows = []

    for group, rate in sex_income_rate.items():
        rows.append(
            {
                "audit_check": "High-income rate by sex",
                "group": group,
                "metric": "positive_outcome_rate_percent",
                "value": float(rate),
            }
        )

    for group, rate in race_income_rate.items():
        rows.append(
            {
                "audit_check": "High-income rate by race",
                "group": group,
                "metric": "positive_outcome_rate_percent",
                "value": float(rate),
            }
        )

    rows.extend(
        [
            {
                "audit_check": "Overall model",
                "group": "all",
                "metric": "accuracy",
                "value": round(
                    model_results["accuracy"],
                    4
                ),
            },
            {
                "audit_check": "Overall model",
                "group": "all",
                "metric": "precision",
                "value": round(
                    model_results["precision"],
                    4
                ),
            },
            {
                "audit_check": "Overall model",
                "group": "all",
                "metric": "recall",
                "value": round(
                    model_results["recall"],
                    4
                ),
            },
        ]
    )

    results_df = pd.DataFrame(rows)

    results_df.to_csv(
        "audit_results.csv",
        index=False
    )

    return results_df


def main():

    print("=" * 70)
    print("RESPONSIBLE AI BIAS, PRIVACY AND RISK AUDIT")
    print("=" * 70)

    df = load_dataset()

    print("\nDataset shape before cleaning:")
    print(df.shape)

    df = clean_dataset(df)

    print("\nDataset shape after cleaning:")
    print(df.shape)

    sex_income_rate, race_income_rate = fairness_audit(df)

    model_results = build_model(df)

    create_visualizations(
        df,
        sex_income_rate,
        race_income_rate
    )

    results_df = save_results(
        df,
        sex_income_rate,
        race_income_rate,
        model_results
    )

    print("\n" + "=" * 70)
    print("AUDIT COMPLETE")
    print("=" * 70)

    print("\nGenerated files:")
    print("- audit_results.csv")
    print("- audit_visualization_1.png")
    print("- audit_visualization_2.png")
    print("- audit_visualization_3.png")

    print("\nKey evidence:")
    print("1. Missing values were measured before cleaning.")
    print("2. Income label imbalance was measured.")
    print("3. Demographic representation was measured.")
    print("4. High-income outcome rates were compared across groups.")
    print("5. Overall model performance was measured.")
    print("6. Model performance was compared by sex.")

    print("\nResults preview:")
    print(results_df.to_string(index=False))


if __name__ == "__main__":
    main()