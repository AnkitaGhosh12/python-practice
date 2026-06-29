# Day 4 Practice - Ankita's Python Journey

print("=" * 40)
print("     STUDENT MARKS MANAGEMENT")
print("=" * 40)

# Starting list
students = ["Ankita", "Priya", "Riya", "Suman", "Mita"]
marks =    [83,        76,      91,     55,       88   ]

# Display all students
print("\n--- All Students ---")
for index, name in enumerate(students, start=1):
    print(f"  {index}. {name} → {marks[index-1]}")

# Add a new student
students.append("Tanisha")
marks.append(79)
print(f"\n✅ Tanisha added! Total students: {len(students)}")

# Find topper
highest = max(marks)
topper_index = marks.index(highest)
print(f"\n🌟 Topper: {students[topper_index]} with {highest} marks")

# Find lowest
lowest = min(marks)
weak_index = marks.index(lowest)
print(f"⚠️  Lowest: {students[weak_index]} with {lowest} marks")

# Class average
average = sum(marks) / len(marks)
print(f"📊 Class Average: {average:.2f}")

# Pass / Fail list
print("\n--- Result List ---")
for i in range(len(students)):
    if marks[i] >= 40:
        status = "PASS ✅"
    else:
        status = "FAIL ❌"
    print(f"  {students[i]:10} → {marks[i]:3}  {status}")

# Remove a student
students.remove("Mita")
marks.pop(4)
print(f"\n🗑️  Mita removed. Remaining students: {len(students)}")

print("\n" + "=" * 40)
print("       PROGRAM COMPLETE")
print("=" * 40)