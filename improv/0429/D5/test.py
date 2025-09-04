import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
# from dataclasses import dataclass, asdict

# @dataclass
# class Person:
#     age: int
#     name: str
#     pets: int


# l = [
#     Person(28, "Jessica", 2),
#     Person(13, "Jack", 0),
#     Person(25, "Jonathan", 1)
# ]

# l = [ asdict(p) for p in l]

# df = pd.DataFrame(l)

# print(df.head())

df = pd.read_csv("soubory/diabetes.csv")


# plt.scatter(df.Age, df.Glucose, s=df.Insulin + 5, c=df.Outcome, cmap="bwr", alpha=0.1)
# plt.title("Glucose level by Age")
# plt.xlabel("Age")
# plt.ylabel("Glucose")
# plt.colorbar(label="Outcome")
# plt.grid(True)
# plt.show()

# corr = df.corr()
# sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1)
# plt.title("Feature correlation heatmap")
# plt.show()

# print(
#     df.isnull().sum(),
#     (df == 0).sum(),
#     (df.BloodPressure == 0).sum(),
#     df.mean(),

#     sep="\n\n===\n\n"
# )

# df = df[df.BloodPressure > 0]
# df = df[df.SkinThickness > 0]
# df = df[df.BloodPressure > 0]
# df = df[df.Glucose > 0]
# df = df[df.BMI > 0]
df = df[
    (df.BloodPressure > 0) &
    (df.SkinThickness > 0) &
    (df.BloodPressure > 0) &
    (df.Glucose > 0) &
    (df.BMI > 0)
]

# print(
#     df.describe(),

#     sep="\n\n===\n\n"
# )


high_risk = df[
    (df.Glucose > 140) & (df.BMI > 30)
]

# print(f"High-risk patiens: {len(high_risk)}")
# print(high_risk[["Glucose", "BMI", "Age"]].head())


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

df["Age_Category"] = pd.cut(
    df.Age,
    bins=[20, 29, 39, 49, 59, 69, 100],
    labels=[
        "20s",
        "30s",
        "40s",
        "50s",
        "60s",
        "70+"
    ]
)

df["RiskScore"] = df.Glucose*0.3 + df.BMI*0.5 + df.Age*0.1

# print(df[["BMI", "BMI_Category", "Age_Category", "RiskScore"]].head())
# print(df.Outcome.value_counts(normalize=True))

# print(
#     df.pivot_table(values=["Glucose"], index="BMI_Category", columns=["Outcome"], aggfunc="mean", observed=False),
#     df.pivot_table(values=["Pregnancies"], index="BMI_Category", columns=["Age_Category"], aggfunc="mean", observed=False),

#     sep="\n\n===\n\n"
# )


# df_sorted_age = df.sort_values("Age")
# df_sorted_age["Glucose_ravg"] = df_sorted_age["Glucose"].rolling(window=60).mean()
# df_sorted_age[["Age", "Glucose", "Glucose_ravg"]].plot(x="Age", title="Rolling average of Glucose by Age")
# plt.show()

from statistics import linear_regression
lr = linear_regression(df.Age, df.Pregnancies)

x = np.linspace(df.Age.min(), df.Age.max(), 2)
slope_manual = df.Age.cov(df.Pregnancies) / df.Age.var()
intercept_manual = df.Pregnancies.mean() - (df.Age.mean() * slope_manual)

y_manual = slope_manual * x + intercept_manual
y_stat = lr.slope * x + lr.intercept



plt.grid(True)
plt.scatter(df.Age, df.Pregnancies, marker="o", s=(df.BMI **2)/10)
plt.plot(x, y_manual, color="orange")
plt.plot(x, y_stat, color="green", ls="--")
plt.show()