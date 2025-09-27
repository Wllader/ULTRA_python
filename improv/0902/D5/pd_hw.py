from statistics import linear_regression
import pandas as pd, numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("diabetes.csv")


x = np.linspace(df.Age.min(), df.Age.max(), 2)

lr = linear_regression(df.Age, df.Pregnancies)
y_stat = lr.slope * x + lr.intercept


slope = df.Age.cov(df.Pregnancies) / df.Age.var()
intercept = df.Pregnancies.mean() - (df.Age.mean() * slope)
y_manual = slope * x + intercept


df = df[df.BloodPressure > 0]
df = df[df.Glucose > 0]
df = df[df.SkinThickness > 0]
df = df[df.BMI > 0]

lr = linear_regression(df.Age, df.Pregnancies)
y_stat_filtered = lr.slope * x + lr.intercept


plt.grid(True)
plt.scatter(df.Age, df.Pregnancies, marker=".", c=df.Age, s=df.Pregnancies *10 + 1)
plt.plot(x, y_manual, c="orange")
plt.plot(x, y_stat, c="green", ls="--", alpha=.5)
plt.plot(x, y_stat_filtered, c="red")
plt.show()