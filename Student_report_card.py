# Simple Student Report Card
print("=== Student Report Card ===")

name = input("Enter student name: ")
subjects = ["Math", "Science", "English", "Computer"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter marks for {subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total, "/ 400")
print("Average:", average)

if average >= 75:
    print("Result: DISTINCTION")
elif average >= 60:
    print("Result: FIRST CLASS")
elif average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")