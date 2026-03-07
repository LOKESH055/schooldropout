import pandas as pd
import os
from datetime import datetime

FILE = "interventions_log.csv"

def log_intervention(student_id, intervention, before_att, after_att, before_math, after_math, before_sci, after_sci):

    data = {
        "student_id": student_id,
        "intervention": intervention,
        "date": datetime.today().strftime("%Y-%m-%d"),
        "attendance_before": before_att,
        "attendance_after": after_att,
        "math_before": before_math,
        "math_after": after_math,
        "science_before": before_sci,
        "science_after": after_sci
    }

    df = pd.DataFrame([data])

    if os.path.exists(FILE):
        old = pd.read_csv(FILE)
        df = pd.concat([old, df], ignore_index=True)

    df.to_csv(FILE, index=False)


def track_progress(student_id):

    if not os.path.exists(FILE):
        return pd.DataFrame()

    df = pd.read_csv(FILE)

    return df[df["student_id"] == student_id]