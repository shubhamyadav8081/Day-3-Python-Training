
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Bar Chart: Number of students in five branches
branches = ["CSE", "IT", "ECE", "ME", "CE"]
students = [120, 100, 80, 60, 50]

plt.figure(figsize=(7, 4))
plt.bar(branches, students)
plt.title("Students in Five Branches")
plt.xlabel("Branch")
plt.ylabel("Number of Students")
plt.show()


# 2. Line Chart: Monthly temperature
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [15, 18, 24, 30, 35, 38, 33, 32, 31, 27, 22, 17]

plt.figure(figsize=(8, 4))
plt.plot(months, temperature, marker="o")
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()


# 3. Scatter Plot: Study hours and marks
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 80, 90]

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()


# 4. Histogram: Marks of 100 students
import random
random.seed(10)
student_marks = [random.randint(0, 100) for _ in range(100)]

plt.figure(figsize=(7, 4))
plt.hist(student_marks, bins=10, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


# 5. Heatmap: Attendance of five subjects over six weeks
attendance = pd.DataFrame(
    [
        [90, 85, 95, 80, 90, 88],
        [80, 85, 90, 85, 80, 95],
        [95, 90, 85, 90, 95, 92],
        [75, 80, 85, 90, 80, 85],
        [85, 90, 80, 85, 95, 90]
    ],
    index=["Maths", "Python", "DSA", "Physics", "English"],
    columns=["Week 1", "Week 2", "Week 3",
             "Week 4", "Week 5", "Week 6"]
)

plt.figure(figsize=(9, 5))
sns.heatmap(attendance, annot=True, cmap="YlGnBu", vmin=0, vmax=100)
plt.title("Subject Attendance Over Six Weeks")
plt.xlabel("Weeks")
plt.ylabel("Subjects")
plt.tight_layout()
plt.show()
