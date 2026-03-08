# AI Early Warning System for School Dropout Prevention

An AI-powered dashboard for **teachers** and **district officers** to predict student dropout risk, recommend interventions, track progress, and visualize district-level dropout risk trends.

---

## Features

### Teacher Dashboard
- Add and manage students.
- Predict dropout risk for individual students using **ML-based or rule-based fallback**.
- View top risk factors for each student.
- Recommend interventions tailored to student needs.
- Communicate with parents in multiple languages.
- Track outcomes of interventions (attendance, math, science scores).
- Compare student performance with class averages.

### District Officer Dashboard
- Visualize district-level dropout risk using a heatmap.
- Monitor district average attendance and risk trends.

---

## Technologies Used
- **Python**  
- **Streamlit** for interactive web dashboards  
- **Pandas** for data manipulation  
- **Matplotlib** for plotting district heatmaps  
- **Scikit-learn** for ML model training (Random Forest Classifier)  
- **Pickle** for saving/loading ML models and encoders  

---

## Project Structure
├── app.py # Main Streamlit app
├── model.py # Train and save ML model
├── risk_predictor.py # ML prediction and rule-based fallback
├── district_heatmap.py # District-level heatmap generation
├── interventions.py # Rule-based interventions
├── parent_message.py # Generates parent communication messages
├── scheme_matcher.py # Match students to government schemes
├── outcome_tracker.py # Track intervention outcomes
├── generate_data.py # Sample data generation
├── students.csv # Student dataset
├── model.pkl # Saved ML model
├── encoders.pkl # Saved encoders for categorical features
└── README.md # Project documentation


---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/LOKESH055/schooldropout.git
cd schooldropout

2,Create and activate virtual environment

  python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

3.Install dependencies

 pip install -r requirements.txt

4.Run the Streamlit app

 streamlit run app.py

5.Open the app in your browser

 The URL will usually be http://localhost:8501.

How It Works

 1.Add student data (attendance, grades, family background).

 2.Predict dropout risk using a Random Forest ML model.

 3.Top risk factors are identified for targeted interventions.

 4.Recommended interventions are suggested to reduce dropout risk.

 5.Parent communication messages can be generated in multiple languages.

 6.District-level heatmaps visualize risk trends for monitoring.

 7.Track intervention outcomes to analyze impact over time.

Notes

The ML model is trained on historical student data (students.csv).

Rule-based predictions act as a fallback when new categories appear in student data.

Ensure that model.pkl and encoders.pkl are in the root directory for ML predictions.

License

This project is MIT Licensed.

