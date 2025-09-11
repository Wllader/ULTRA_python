import pandas as pd, numpy as np, matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("diabetes.csv")

# print(
#     df.head()
# )


# plt.scatter(df.Age, df.Glucose, s=df.Insulin + 5, c=df.Outcome, cmap="bwr", alpha=.1)
# plt.title("Glucose level by age")
# plt.xlabel("Age")
# plt.ylabel("Glucose")
# plt.colorbar()
# plt.grid(True)
# plt.show()

# corr = df.corr()
# sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1)
# plt.title("Feature correlation heatmap")
# plt.tight_layout()
# plt.show()

# print(
#     (df == 0).sum()
# )

# high_risk = df[
#     (df.Glucose > 140) & (df.BMI > 30)
# ]

# print(f"High-risk patients: {len(high_risk)}")
# print(
#     high_risk[["Glucose", "BMI", "Age"]]
# )


df["BMI_Category"] = pd.cut(
    df.BMI,
    bins=[0, 18.5, 25, 30, 35, 100],
    labels=[
        "Underweight",
        "Normal",
        "Overweight",
        "Obese",
        "Extremely obese"
    ]
)

df["RiskScore"] = df.Glucose*0.3 + df.BMI*0.2 + df.Age*0.1

df["Age_Category"] = pd.cut(
    df.Age,
    bins=[20, 30, 40, 50, 60, 70, 100],
    labels=[
        "20s",
        "30s",
        "40s",
        "50s",
        "60s",
        "70+"
    ]
)


# print(df[["BMI", "BMI_Category", "Age_Category", "RiskScore"]])
# print(df[df["Age_Category"] == "40s"]["BMI"])

# print(
#     (df == 0).sum()
# )

df = df[df.BloodPressure > 0]
df = df[df.Glucose > 0]
df = df[df.SkinThickness > 0]
df = df[df.BMI > 0]

# print(df)

# print(df.Outcome.value_counts())
# print(df.Outcome.value_counts(normalize=True))


# print(
#     df.pivot_table(values=["Glucose", "Age"], index="BMI_Category", columns=["Outcome"], aggfunc="mean", observed=False),
#     df.pivot_table(values=["Pregnancies"], index="BMI_Category", columns=["Age_Category"], aggfunc="mean", observed=False),

#     sep="\n--\n"
# )


# df_sorted = df.sort_values("BloodPressure")
# df_sorted["Glucose_Rolling"] = df_sorted["Glucose"].rolling(window=60).mean()
# df_sorted[["BloodPressure", "Glucose", "Glucose_Rolling"]].plot(x="BloodPressure", title="Rolling average of Glucose")
# plt.show()


# print(
#     df.groupby(["Age_Category", "Outcome"], observed=False)["Glucose"].mean()
# )

from statistics import linear_regression