def match_schemes(student):

    schemes = []

    if student["income_level"]=="Low":
        schemes.append("Pre-Matric Scholarship")

    if student["gender"]=="Female":
        schemes.append("Beti Bachao Beti Padhao")

    if student["distance"]>5:
        schemes.append("Free Bicycle Scheme")

    if student["meal"]=="No":
        schemes.append("Mid-Day Meal Scheme")

    return schemes