import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("students.csv")

# Create dropout risk label (synthetic)
df["dropout_risk"] = (
    (df["attendance"] < 60) |
    (df["math"] < 40) |
    (df["science"] < 40) |
    (df["sibling_dropout"] == "Yes") |
    (df["income_level"] == "Low")
).astype(int)

# Features
X = df.drop(columns=["dropout_risk","student_id"])
y = df["dropout_risk"]

# Encode categorical columns
categorical_cols = [
    "district",
    "gender",
    "meal",
    "sibling_dropout",
    "father_present",
    "mother_present",
    "income_level"
]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X,y)

# Save model
with open("model.pkl","wb") as f:
    pickle.dump(model,f)

# Save encoders
with open("encoders.pkl","wb") as f:
    pickle.dump(encoders,f)

print("Model trained and saved")