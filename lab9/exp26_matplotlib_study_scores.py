"""
Experiment 26: Visualize distribution and relationship between students' study hours
and examination scores using histograms and scatter plots.
"""
import numpy as np
import matplotlib.pyplot as plt

students = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]
exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

axes[0].hist(study_hours, bins=5, color="#4c78a8", edgecolor="black")
axes[0].set_title("Distribution of Study Hours/Week")
axes[0].set_xlabel("Study Hours / Week")
axes[0].set_ylabel("Number of Students")

axes[1].hist(exam_scores, bins=5, color="#54a24b", edgecolor="black")
axes[1].set_title("Distribution of Exam Scores")
axes[1].set_xlabel("Exam Score")
axes[1].set_ylabel("Number of Students")

axes[2].scatter(study_hours, exam_scores, color="#e45756", s=70, label="Students")
m, b = np.polyfit(study_hours, exam_scores, 1)
x_vals = np.array(sorted(study_hours))
axes[2].plot(x_vals, m * x_vals + b, color="black", linestyle="--", label="Trendline")
axes[2].set_title("Study Hours vs Exam Score")
axes[2].set_xlabel("Study Hours / Week")
axes[2].set_ylabel("Exam Score")
axes[2].legend()
axes[2].grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
plt.savefig("study_hours_vs_scores.png", dpi=150)
plt.show()
