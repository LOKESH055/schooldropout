import pandas as pd
import matplotlib.pyplot as plt
from risk_predictor import predict_risk


def generate_heatmap(students):

    df = students.copy()

    # Calculate risk score for each student
    risk_scores = []

    for _, row in df.iterrows():
        risk_score, _ = predict_risk(row)
        risk_scores.append(risk_score)

    df["risk_score"] = risk_scores

    # District average risk
    district_risk = df.groupby("district")["risk_score"].mean()

    heatmap_data = district_risk.to_frame(name="Dropout Risk")

    fig, ax = plt.subplots(figsize=(6,4))

    heatmap = ax.imshow(
        heatmap_data,
        cmap="Reds",
        aspect="auto"
    )

    # Axis labels
    ax.set_xticks([0])
    ax.set_xticklabels(["Risk Level"])

    ax.set_yticks(range(len(heatmap_data.index)))
    ax.set_yticklabels(heatmap_data.index)

    # Title
    ax.set_title("District Level Dropout Risk Heatmap")

    # Add values inside heatmap
    for i in range(len(heatmap_data.index)):
        value = heatmap_data.iloc[i,0]
        ax.text(
            0, i,
            f"{value:.1f}%",
            ha="center",
            va="center",
            color="black"
        )

    fig.colorbar(heatmap)

    return fig