import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# ------------------------------
# Load dataset
# ------------------------------
df = pd.read_csv("students.csv")

# ------------------------------
# Features and target
# ------------------------------
X = df.drop(columns=["dropout_risk", "student_id"])  # Features
y = df["dropout_risk"]  # Target from generate_data.py (0-100 risk score)

# ------------------------------
# Encode categorical columns
# ------------------------------
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

# ------------------------------
# Train model
# ------------------------------
model = RandomForestClassifier(
    n_estimators=200,        # Increased for better learning
    random_state=42,
    class_weight="balanced", # Helps with imbalanced dropout_risk
)
model.fit(X, y)

# ------------------------------
# Save model and encoders
# ------------------------------
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("ML Model trained and saved using dropout_risk from dataset")
