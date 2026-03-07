def recommend_interventions(student):

    interventions = []

    if student["attendance"] < 70:
        interventions.append("Student counseling for attendance")

    if student["math"] < 50 or student["science"] < 50:
        interventions.append("Provide remedial classes")

    if student["distance"] > 5:
        interventions.append("Provide transport support")

    if student["income_level"] == "Low":
        interventions.append("Recommend scholarship scheme")

    if student["sibling_dropout"] == "Yes":
        interventions.append("Family counseling")

    if student["meal"] == "No":
        interventions.append("Enroll in Midday Meal Scheme")

    if len(interventions)==0:
        interventions.append("Regular monitoring")

    return interventions