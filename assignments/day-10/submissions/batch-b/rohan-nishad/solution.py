import matplotlib.pyplot as plt
from pathlib import Path

base_dir = Path(__file__).resolve().parent

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_sales = [12000, 15000, 13500, 18000, 21000, 19500]
courses = ["Python", "Data Analytics", "AI", "Machine Learning"]
students = [35, 28, 22, 18]

plt.figure(figsize=(6, 4))
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(base_dir / "monthly_sales_line.png")
plt.close()

plt.figure(figsize=(6, 4))
plt.bar(courses, students)
plt.title("Students by Course")
plt.xlabel("Course")
plt.ylabel("Students")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(base_dir / "students_by_course_bar.png")
plt.close()

plt.figure(figsize=(6, 6))
plt.pie(students, labels=courses, autopct='%1.1f%%')
plt.title("Course Enrollment Share")
plt.tight_layout()
plt.savefig(base_dir / "course_enrollment_pie.png")
plt.close()

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 55, 62, 70, 82, 90]

plt.figure(figsize=(6, 4))
plt.scatter(study_hours, marks)
plt.title("Study Hours and Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(base_dir / "study_hours_scatter.png")
plt.close()

plt.figure(figsize=(6, 4))
plt.plot(months, monthly_sales, marker='o', label='Sales')
plt.grid(True)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig(base_dir / "monthly_sales_line_grid.png")
plt.close()

python_students = [20, 25, 30, 28, 35, 40]
ai_students = [10, 12, 15, 18, 20, 22]

plt.figure(figsize=(6, 4))
plt.plot(months, python_students, marker='o', label='Python')
plt.plot(months, ai_students, marker='o', label='AI')
plt.title("Course Growth")
plt.xlabel("Month")
plt.ylabel("Students")
plt.legend()
plt.tight_layout()
plt.savefig(base_dir / "course_growth.png")
plt.close()

# A bar chart is best for comparing courses because it makes differences in student counts easy to see at a glance.
