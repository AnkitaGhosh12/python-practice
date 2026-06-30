# Types of Functions
# Type 1 — No parameter, no return
def show_header():
    print("=" * 30)
    print("  STUDENT MANAGEMENT SYSTEM")
    print("=" * 30)

show_header()

# Type 2 — Has parameter, no return
def show_student(name):
    print(f"Student: {name}")

show_student("Ankita")

# Type 3 — No parameter, has return
def get_school():
    return "Canning Government Polytechnic"

school = get_school()
print(school)

# Type 4 — Has parameter, has return (most useful!)
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

print(calculate_grade(83))   # B
print(calculate_grade(91))   # A
print(calculate_grade(35))   # F