import pandas as pd
import pickle
import numpy as np

# Load ML model and encoders
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)


# -------------------------------
# Rule-based fallback
# -------------------------------
def compute_risk_score(student):
    score = 0
    if student["attendance"] < 70:
        score += 30
    if student["math"] < 50:
        score += 20
    if student["science"] < 50:
        score += 20
    if student["income_level"] == "Low":
        score += 20
    if student["sibling_dropout"] == "Yes":
        score += 10
    return min(score, 100)


def compute_top_factors(student):
    factors = []
    if student["attendance"] < 70:
        factors.append("attendance")
    if student["math"] < 50:
        factors.append("math")
    if student["science"] < 50:
        factors.append("science")
    if student["income_level"] == "Low":
        factors.append("income_level")
    if student["sibling_dropout"] == "Yes":
        factors.append("sibling_dropout")
    return factors[:3]


# -------------------------------
# ML prediction with fallback
# -------------------------------
def predict_risk_ml(student):
    df = pd.DataFrame([student])
    if "student_id" in df.columns:
        df = df.drop(columns=["student_id"])
    categorical_cols = ["district", "gender", "meal", "sibling_dropout", "father_present", "mother_present",
                        "income_level"]

    try:
        for col in categorical_cols:
            if df[col].iloc[0] not in encoders[col].classes_:
                raise ValueError(f"Unknown category {df[col].iloc[0]} in {col}")
            df[col] = encoders[col].transform(df[col])

        prob = model.predict_proba(df)[0][1]
        risk_score = prob * 100

        importances = model.feature_importances_
        features = df.columns
        idx = np.argsort(importances)[-3:][::-1]
        top_factors = [features[i] for i in idx]
        return risk_score, top_factors
    except:
        # fallback to rule-based
        return compute_risk_score(student), compute_top_factors(student)
