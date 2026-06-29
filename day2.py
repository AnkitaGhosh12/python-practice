print("=" * 35)
print("  STUDENT RESULT CHECKER ")
print("=" * 35)

name = input("Enter student name: ")
marks = int(input("Enter marks (out of 100): "))
attendance = int(input("Enter attendance % :"))

if marks >= 90:
    grade = "A - Excellent"
elif marks >=75:
    grade = "B - Good"
elif marks >= 60:
    grade = "C - Average"
elif marks >= 40:
    grade="D - Below Average"
else:
    grade = "F - Failed"

if marks >= 40 and attendance >=75:
    result = "Pass"
elif marks >= 40 and attendance < 75:
    result = "Detained (Low attendance)"
else:
    result = "Fail"

print("-" * 35)
print(f"  Name      : {name}")
print(f"  Marks     : {marks}/100")
print(f"  Attendance: {attendance}%")
print(f"  Grade     : {grade}")
print(f"  Result    : {result}")
print("-" * 35)