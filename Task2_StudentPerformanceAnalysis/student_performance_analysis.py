import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv("student_performance.csv")

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Calculate average marks
subjects = ["Maths", "Science", "English"]
df["Average_Marks"] = df[subjects].mean(axis=1)

# Display basic analysis
print("STUDENT PERFORMANCE ANALYSIS")
print("-" * 35)

print("\nFirst 5 Students:")
print(df.head())

print("\nAverage Marks by Subject:")
print(df[subjects].mean())

print("\nOverall Class Average:")
print(round(df["Average_Marks"].mean(), 2))

print("\nHighest Student Average:")
print(round(df["Average_Marks"].max(), 2))

print("\nAverage Marks by Study Hours:")
print(df.groupby("Study_Hours")["Average_Marks"].mean())

# Graph 1: Average marks by subject
subject_averages = df[subjects].mean()

plt.figure(figsize=(8, 5))
subject_averages.plot(kind="bar", color="skyblue")
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("outputs/subject_averages.png", dpi=300)
plt.close()

# Graph 2: Student-wise average marks
plt.figure(figsize=(10, 5))
plt.bar(df["Student_ID"], df["Average_Marks"], color="orange")
plt.title("Student-wise Average Marks")
plt.xlabel("Student ID")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("outputs/student_averages.png", dpi=300)
plt.close()

# Graph 3: Study hours vs average marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Average_Marks"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Daily Study Hours")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("outputs/study_hours_vs_marks.png", dpi=300)
plt.close()

print("\nAnalysis completed successfully!")
print("Graphs saved in the outputs folder.")