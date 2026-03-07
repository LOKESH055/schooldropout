import streamlit as st
import pandas as pd

from risk_predictor import predict_risk
from interventions import recommend_interventions
from parent_message import generate_parent_message
from scheme_matcher import match_schemes
from district_heatmap import generate_heatmap
from outcome_tracker import log_intervention, track_progress

students = pd.read_csv("students.csv")

st.title("AI Early Warning System for School Dropout Prevention")

# Sidebar navigation
view = st.sidebar.selectbox(
    "Select Dashboard",
    ["Teacher Dashboard", "District Officer Dashboard"]
)

# -------------------------
# DISTRICT DASHBOARD
# -------------------------

if view == "District Officer Dashboard":

    st.header("District Risk Monitoring")

    fig = generate_heatmap(students)

    st.pyplot(fig)

    st.subheader("District Average Attendance")

    district_avg = students.groupby("district")["attendance"].mean()

    st.dataframe(district_avg)

# -------------------------
# TEACHER DASHBOARD
# -------------------------

if view == "Teacher Dashboard":

    st.header("Teacher Early Warning Dashboard")

    student_ids = students["student_id"].tolist()

    selected_id = st.selectbox(
        "Select Student",
        student_ids,
        key="student_selector"
    )

    # Reset prediction when student changes
    if "previous_student" not in st.session_state:
        st.session_state.previous_student = selected_id

    if st.session_state.previous_student != selected_id:
        if "risk_score" in st.session_state:
            del st.session_state["risk_score"]
        if "factors" in st.session_state:
            del st.session_state["factors"]

        st.session_state.previous_student = selected_id

    student = students[students["student_id"] == selected_id].iloc[0]

    st.subheader("Student Information")

    st.write("District:", student["district"])
    st.write("Gender:", student["gender"])
    st.write("Attendance:", student["attendance"])
    st.write("Math:", student["math"])
    st.write("Science:", student["science"])
    st.write("Distance:", student["distance"])
    st.write("Midday Meal:", student["meal"])
    st.write("Sibling Dropout:", student["sibling_dropout"])
    st.write("Income Level:", student["income_level"])

    # -------------------------
    # Predict Risk
    # -------------------------

    if st.button("Predict Dropout Risk"):

        risk_score, factors = predict_risk(student)

        st.session_state["risk_score"] = risk_score
        st.session_state["factors"] = factors

    # -------------------------
    # SHOW RESULTS
    # -------------------------

    if "risk_score" in st.session_state:

        risk_score = st.session_state["risk_score"]
        factors = st.session_state["factors"]

        st.subheader("Dropout Risk Score")

        st.success(f"{risk_score:.2f}%")

        st.subheader("Top Risk Factors")

        for f in factors:
            st.write("•", f)

        # Cohort comparison
        st.subheader("Cohort Comparison")

        class_avg_att = students["attendance"].mean()
        class_avg_math = students["math"].mean()

        st.write("Student Attendance:", student["attendance"])
        st.write("Class Average Attendance:", round(class_avg_att,2))

        st.write("Student Math:", student["math"])
        st.write("Class Average Math:", round(class_avg_math,2))

        # Interventions
        st.subheader("Recommended Interventions")

        interventions = recommend_interventions(student)

        for i in interventions:
            st.write("•", i)

        # Parent communication
        st.subheader("Parent Communication")

        language = st.selectbox(
            "Select Language",
            ["English","Hindi","Tamil"]
        )

        msg = generate_parent_message(student,language)

        st.write(msg)

        # Government schemes
        st.subheader("Eligible Government Schemes")

        schemes = match_schemes(student)

        for s in schemes:
            st.write("•", s)

        # --------------------------------------------------
        # OUTCOME TRACKER
        # --------------------------------------------------

        st.subheader("Intervention Outcome Tracker")

        with st.form("outcome_form"):

            selected_intervention = st.multiselect(
                "Select Intervention Applied",
                interventions
            )

            new_attendance = st.number_input(
                "Attendance After Intervention",
                0,100
            )

            new_math = st.number_input(
                "Math Score After Intervention",
                0,100
            )

            new_science = st.number_input(
                "Science Score After Intervention",
                0,100
            )

            submit = st.form_submit_button("Log Intervention Outcome")

            if submit:

                log_intervention(
                    student["student_id"],
                    selected_intervention,
                    student["attendance"],
                    new_attendance,
                    student["math"],
                    new_math,
                    student["science"],
                    new_science
                )

                st.success("Intervention outcome logged successfully!")

                # --------------------------------------------------
                # NEW FEATURE: CHECK IF INTERVENTION WORKED
                # --------------------------------------------------

                st.subheader("Intervention Impact Analysis")

                # Create updated student data
                updated_student = student.copy()

                updated_student["attendance"] = new_attendance
                updated_student["math"] = new_math
                updated_student["science"] = new_science

                # Predict new risk
                new_risk, new_factors = predict_risk(updated_student)

                st.write("Previous Risk Score:", f"{risk_score:.2f}%")
                st.write("New Risk Score:", f"{new_risk:.2f}%")

                # Compare risks
                if new_risk < risk_score:

                    st.success(
                        "The intervention appears to be effective. "
                        "The student's dropout risk has decreased."
                    )

                elif new_risk > risk_score:

                    st.error(
                        "Warning: The dropout risk has increased. "
                        "Additional intervention may be required."
                    )

                else:

                    st.warning(
                        "The student's risk level remains unchanged."
                    )

        # ------------------------------
        # HISTORY
        # ------------------------------

        st.subheader("Student Intervention History")

        history = track_progress(student["student_id"])

        if not history.empty:
            st.dataframe(history)
        else:
            st.write("No intervention records found yet.")