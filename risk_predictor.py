import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl","rb"))
encoders = pickle.load(open("encoders.pkl","rb"))

def predict_risk(student):

    df = pd.DataFrame([student])

    if "student_id" in df.columns:
        df = df.drop(columns=["student_id"])

    categorical_cols = [
        "district",
        "gender",
        "meal",
        "sibling_dropout",
        "father_present",
        "mother_present",
        "income_level"
    ]

    for col in categorical_cols:
        df[col] = encoders[col].transform(df[col])

    prob = model.predict_proba(df)[0][1]

    risk_score = prob * 100

    importances = model.feature_importances_
    features = df.columns

    idx = importances.argsort()[-3:][::-1]

    top_factors = [features[i] for i in idx]

    return risk_score, top_factors