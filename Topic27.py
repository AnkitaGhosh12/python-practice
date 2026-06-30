# Calling Functions Inside Functions
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)     # calling square() inside this function

result = sum_of_squares(3, 4)
print(result)    # 9 + 16 = 25

# Practical example — student grading system:
def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

def show_report(name, marks):
    avg = calculate_average(marks)        # calling function 1
    grade = calculate_grade(avg)          # calling function 2 (using result of function 1)
    print(f"{name}: Average = {avg:.2f}, Grade = {grade}")

show_report("Ankita", [83, 91, 76, 88])
show_report("Priya",  [95, 98, 92, 97])