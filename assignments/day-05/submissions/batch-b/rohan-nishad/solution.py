from pathlib import Path

base_dir = Path(__file__).resolve().parent

student_file = base_dir / "student.txt"
student_file.write_text("Name: Rohan\nAge: 20\nCollege: BIT\n", encoding="utf-8")
print("File created successfully")

content = student_file.read_text(encoding="utf-8")
print(content, end="")

student_file.write_text(content + "Course: Python Data AI\nCity: Gorakhpur\n", encoding="utf-8")
updated_content = student_file.read_text(encoding="utf-8")
print(updated_content, end="")

lines = student_file.read_text(encoding="utf-8").splitlines()
print(f"Total lines: {len(lines)}")

students_file = base_dir / "students.txt"
students_file.write_text("Aman\nPriya\nShalu\nRaj\nAnsh\n", encoding="utf-8")
print(students_file.read_text(encoding="utf-8"), end="")

name = input("Enter a student name: ").strip()
print("Found" if name in students_file.read_text(encoding="utf-8").splitlines() else "Not Found")

backup_file = base_dir / "students_backup.txt"
backup_file.write_text(students_file.read_text(encoding="utf-8"), encoding="utf-8")
print("Backup created successfully")

marks_file = base_dir / "marks.txt"
marks_file.write_text("85\n90\n78\n92\n88\n", encoding="utf-8")
marks = [int(line.strip()) for line in marks_file.read_text(encoding="utf-8").splitlines() if line.strip()]
total = sum(marks)
average = total / len(marks)
print(f"Total marks: {total}")
print(f"Average marks: {average}")
