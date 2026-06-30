# Day 5 Practice - Ankita's Python Journey

# ── Function definitions ──────────────────

def show_header():
    print("=" * 40)
    print("      STUDENT REPORT CARD SYSTEM")
    print("=" * 40)

def calculate_grade(marks):
    if marks >= 90:
        return "A ⭐"
    elif marks >= 75:
        return "B 👍"
    elif marks >= 60:
        return "C 🙂"
    elif marks >= 40:
        return "D ⚠️"
    else:
        return "F ❌"

def calculate_stats(marks_list):
    total   = sum(marks_list)
    average = total / len(marks_list)
    highest = max(marks_list)
    lowest  = min(marks_list)
    return total, average, highest, lowest

def show_result(name, marks_list):
    print(f"\n  Student : {name}")
    print(f"  Marks   : {marks_list}")
    total, avg, high, low = calculate_stats(marks_list)
    print(f"  Total   : {total}")
    print(f"  Average : {avg:.2f}")
    print(f"  Highest : {high}")
    print(f"  Lowest  : {low}")
    print(f"  Grade   : {calculate_grade(avg)}")
    if avg >= 40:
        print(f"  Result  : PASS ✅")
    else:
        print(f"  Result  : FAIL ❌")
    print("-" * 40)

# ── Main program ──────────────────────────

show_header()

show_result("Ankita", [83, 91, 76, 88, 79])
show_result("Priya",  [55, 60, 48, 71, 65])
show_result("Riya",   [95, 98, 92, 97, 99])
show_result("Suman",  [35, 28, 40, 30, 25])