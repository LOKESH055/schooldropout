# AI Early Warning System for School Dropout Prevention

## Background
India has a 19% secondary school dropout rate — roughly 1 in 5 students leaves before Class 10.  
Government schools have attendance registers, exam records, and mid-day meal data but no system that connects these signals to predict which student is at risk.  

This system allows teachers and district officers to **identify at-risk students weeks before dropout**, enabling timely interventions.

---

## Features

### Teacher Dashboard
- Select a student and view **attendance, exam scores, distance, sibling dropout, and income level**.  
- Predict **dropout risk score** with **top 3 contributing factors** explained.  
- **Recommended interventions** for each student.  
- **Parent message generator** in multiple languages (English, Hindi, Tamil).  
- **Cohort comparison** with class average.  
- **Government scheme matcher** for eligible students.  
- **Intervention outcome tracker** to log changes after interventions and check if the student’s risk decreases.  
- Shows **if intervention improved student indicators** (attendance/math/science) and whether risk decreased or increased.

### District Officer Dashboard
- **District-level dropout risk heatmap**.  
- Aggregated anonymized data to help allocate resources.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/edu_guard.git
cd edu_guard
2.Install required Python packages:
Bash
pip install -r requirements.txt

3.Run the app:

streamlit run app.py

Usage

  1.Teacher selects a student from the dashboard.

  2.Click Predict Dropout Risk → view risk score and top risk factors.

  3.Check recommended interventions and generate parent message.

  4.Log intervention outcomes (attendance, math, science after intervention).

  5.View intervention effect: the app shows whether the student improved and whether dropout risk decreased.

  6.District officers can view district-level heatmaps for dropout risk.

License

 This project is licensed under the MIT License.
