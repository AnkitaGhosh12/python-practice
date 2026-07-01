# Looping Through Dictionaries
student = {
    "name"  : "Ankita",
    "age"   : 20,
    "city"  : "Dankuni",
    "marks" : 83.5
}

# Loop through keys only
for key in student:
    print(key)

# Loop through values only
for value in student.values():
    print(value)

# Loop through both key and value (most useful!)
for key, value in student.items():
    print(f"{key} : {value}")

# Practical example:
marks = {
    "Maths"   : 88,
    "Physics" : 76,
    "Python"  : 95,
    "English" : 82
}

total = 0
for subject, mark in marks.items():
    print(f"  {subject:10} → {mark}")
    total += mark

average = total / len(marks)
print(f"\n  Total   : {total}")
print(f"  Average : {average:.2f}")