students = ["Ankita", "Priya", "Riya", "Suman"]

# Method 1 — simple loop
for student in students:
    print(student)

# Method 2 — with index number
for i in range(len(students)):
    print(f"{i+1}. {students[i]}")

# Method 3 — enumerate (best method!)
for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")

marks = [85, 90, 45, 78, 38, 92, 55]

print("Students who failed:")
for mark in marks:
    if mark < 40:
        print(f"  ❌ Marks: {mark}")

print("\nStudents who got A grade:")
for mark in marks:
    if mark >= 90:
        print(f"  🌟 Marks: {mark}")