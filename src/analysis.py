import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/marks.csv")
print(df)

# Calculate total and average marks for each student
df["total"] = df["maths"] + df["science"] + df["english"]
df["average"] = (df["total"] / 3).round(2)
print(df)

# Identify the topper
topper = df.loc[df["total"].idxmax(), "name"]
print("Topper:", topper)

# Calculate the overall class average
class_average = df["average"].mean()
print("Class Average:", round(class_average, 2))