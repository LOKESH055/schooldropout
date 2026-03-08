import pandas as pd
import random
import numpy as np

# Number of students
NUM_STUDENTS = 250

# Possible values
districts = ["Chennai", "Madurai", "Salem", "Coimbatore", "Tirunelveli"]
genders = ["Male", "Female"]
meal_participation = ["Yes", "No"]
yes_no = ["Yes", "No"]
income_levels = ["Low", "Medium", "High"]

data = []

for i in range(NUM_STUDENTS):
    district = random.choice(districts)
    gender = random.choice(genders)
    attendance = random.randint(40, 100)
    math = random.randint(20, 100)
    science = random.randint(20, 100)
    distance = random.randint(0, 20)
    meal = random.choice(meal_participation)
    sibling_dropout = random.choice(yes_no)
    father_present = random.choice(yes_no)
    mother_present = random.choice(yes_no)
    income_level = random.choice(income_levels)

    data.append([
        district, gender, attendance, math, science,
        distance, meal, sibling_dropout, father_present, mother_present, income_level
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "district", "gender", "attendance", "math", "science",
    "distance", "meal", "sibling_dropout", "father_present", "mother_present", "income_level"
])

# Add student_id as first column
df.insert(0, "student_id", ["S" + str(i + 1).zfill(3) for i in range(NUM_STUDENTS)])

# ------------------------------
# ADD TARGET COLUMN (dropout_risk) with randomness for supervised learning
# ------------------------------
def generate_target(row):
    score = 0
    if row['attendance'] < 70:
        score += 30
    if row['math'] < 50:
        score += 20
    if row['science'] < 50:
        score += 20
    if row['income_level'] == 'Low':
        score += 20
    if row['sibling_dropout'] == 'Yes':
        score += 10
    # Add randomness to create supervised learning target
    noise = np.random.randint(-5, 6)  # +/-5%
    score = min(max(score + noise, 0), 100)
    return score

df['dropout_risk'] = df.apply(generate_target, axis=1)

# ------------------------------
# Optional: Convert risk score to binary for classification (0/1)
# ------------------------------
# threshold = 50
# df['dropout_risk'] = (df['dropout_risk'] >= threshold).astype(int)

# Save to CSV
df.to_csv("students.csv", index=False)
print("students.csv generated with student_id, 250 students, and dropout_risk column!")
