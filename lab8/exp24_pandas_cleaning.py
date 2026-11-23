"""
Experiment 24: Clean and preprocess a real-world dataset using Pandas.
"""
import numpy as np
import pandas as pd

raw_data = {
    "Employee_ID": [101, 102, 103, 103, 104, 105, 106, 107],
    "Name": ["  alice verma ", "BOB SINGH", "Charu Patel", "Charu Patel", "dev kumar", None, "Esha Roy ", "Farhan Ali"],
    "Department": ["it", "HR ", "Finance", "Finance", "IT", "hr", "Sales", "IT"],
    "Age": [28, 34, np.nan, np.nan, 29, 41, 150, 31],
    "Salary_INR": ["65000", "72000", "80000", "80000", None, "91000", "58000", "76000"],
}

df = pd.DataFrame(raw_data)
print("=== RAW DATASET ===")
print(df, "\n")

df = df.drop_duplicates(subset=["Employee_ID"]).copy()
df["Name"] = df["Name"].fillna("Unknown Employee").str.strip().str.title()
df["Department"] = df["Department"].str.strip().str.upper()

df["Salary_INR"] = pd.to_numeric(df["Salary_INR"], errors="coerce")
df["Salary_INR"] = df["Salary_INR"].fillna(df["Salary_INR"].median())

df.loc[df["Age"] > 100, "Age"] = np.nan
df["Age"] = df["Age"].fillna(df["Age"].median()).astype(int)

df["Annual_CTC_Lakhs"] = (df["Salary_INR"] * 12 / 100000).round(2)

df.to_csv("cleaned_employees.csv", index=False)
print("=== CLEANED DATASET ===")
print(df)
