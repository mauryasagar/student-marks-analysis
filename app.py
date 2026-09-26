import streamlit as st
import pandas as pd

# Add a title to the web page
st.title("Student Marks Analysis")

# Load the data
df = pd.read_csv("data/marks.csv")

# Calculate total and average marks for each student
df["total"] = df["maths"] + df["science"] + df["english"]
df["average"] = (df["total"] / 3).round(2)

# Determine pass/fail
df["result"] = df[["maths", "science", "english"]].apply(
    lambda row: "Pass" if all(row >= 40) else "Fail", axis=1
)

# Display the data as an interactive table
st.dataframe(df)