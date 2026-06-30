total_students = 0    # global variable

def add_student():
    global total_students
    total_students += 1

def calculate_stats(marks):
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)
    return highest, lowest, average        # multiple return values

def get_grade(average):
    if average >= 90:
        return "A ⭐"
    elif average >= 75:
        return "B 👍"
    elif average >= 60:
        return "C 🙂"
    elif average >= 40:
        return "D ⚠️"
    else:
        return "F ❌"

def show_report(name, marks):
    add_student()                                    # calling function inside function
    high, low, avg = calculate_stats(marks)           # calling function inside function
    grade = get_grade(avg)                            # calling function inside function

    print(f"\n  Student : {name}")
    print(f"  Marks   : {marks}")
    print(f"  Highest : {high}")
    print(f"  Lowest  : {low}")
    print(f"  Average : {avg:.2f}")
    print(f"  Grade   : {grade}")
    print("-" * 35)

# ── Main Program ──────────────────────────

print("=" * 35)
print("   STUDENT REPORT - WEEK 2")
print("=" * 35)

show_report("Ankita", [83, 91, 76, 88, 79])
show_report("Priya",  [55, 60, 48, 71, 65])
show_report("Riya",   [95, 98, 92, 97, 99])

print(f"\n📊 Total students processed: {total_students}")