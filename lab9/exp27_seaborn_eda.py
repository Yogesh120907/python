"""
Experiment 27: Exploratory Data Analysis on student examination data using Seaborn
(subject-wise score distributions, pairwise relationships, and correlation heatmap).
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics": [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry": [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English": [80, 84, 72, 91, 76, 80, 70, 95, 77, 89],
}

df = pd.DataFrame(data)
subjects = ["Mathematics", "Physics", "Chemistry", "English"]

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

melted = df.melt(id_vars="Student", value_vars=subjects, var_name="Subject", value_name="Score")
sns.boxplot(data=melted, x="Subject", y="Score", hue="Subject", palette="Set2", legend=False, ax=axes[0])
sns.stripplot(data=melted, x="Subject", y="Score", color="black", size=6, ax=axes[0])
axes[0].set_title("Subject-Wise Score Distributions")

corr = df[subjects].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=axes[1])
axes[1].set_title("Subject Score Correlation Heatmap")

plt.tight_layout()
plt.savefig("seaborn_distributions_heatmap.png", dpi=150)

pair_grid = sns.pairplot(df[subjects], diag_kind="kde", corner=False)
pair_grid.fig.suptitle("Pairwise Relationships Across Subjects", y=1.02)
pair_grid.savefig("seaborn_pairplot.png", dpi=150)

plt.show()
