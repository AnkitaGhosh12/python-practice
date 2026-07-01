# Day 8 Practice - Ankita's Python Journey

students = {
    "Ankita" : {
        "age"   : 20,
        "city"  : "Dankuni",
        "marks" : {
            "Maths"   : 88,
            "Physics" : 76,
            "Python"  : 95,
            "English" : 82
        }
    },
    "Priya" : {
        "age"   : 19,
        "city"  : "Kolkata",
        "marks" : {
            "Maths"   : 92,
            "Physics" : 88,
            "Python"  : 97,
            "English" : 90
        }
    },
    "Riya" : {
        "age"   : 20,
        "city"  : "Howrah",
        "marks" : {
            "Maths"   : 65,
            "Physics" : 70,
            "Python"  : 78,
            "English" : 60
        }
    }
}

print("=" * 45)
print("      STUDENT DICTIONARY REPORT")
print("=" * 45)

for name, info in students.items():
    marks = info["marks"]
    total   = sum(marks.values())
    average = total / len(marks)

    if average >= 90:
        grade = "A ⭐"
    elif average >= 75:
        grade = "B 👍"
    elif average >= 60:
        grade = "C 🙂"
    else:
        grade = "D ⚠️"

    print(f"\n  Name    : {name}")
    print(f"  Age     : {info['age']}")
    print(f"  City    : {info['city']}")
    print(f"  Marks   :")
    for subject, mark in marks.items():
        print(f"    {subject:10} → {mark}")
    print(f"  Total   : {total}")
    print(f"  Average : {average:.2f}")
    print(f"  Grade   : {grade}")
    print("-" * 45)