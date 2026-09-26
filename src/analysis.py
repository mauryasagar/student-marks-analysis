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

# Determine pass/fail (pass = 40 or more in all subjects)
df["result"] = df[["maths", "science", "english"]].apply(
    lambda row: "Pass" if all(row >= 40) else "Fail", axis=1
)
print(df[["name", "average", "result"]])

# Create a bar chart of average marks
plt.figure(figsize=(8, 5))
plt.bar(df["name"], df["average"], color="steelblue")
plt.title("Average Marks per Student")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/average_marks.png")