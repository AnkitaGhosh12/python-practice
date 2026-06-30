def get_student_info():
    name = "Ankita"
    age = 20
    marks = 83.5
    return name, age, marks      # returns 3 values

# Unpacking into 3 variables
n, a, m = get_student_info()
print(n)   # Ankita
print(a)   # 20
print(m)   # 83.5

# Real example — min, max, average together:
def get_stats(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    average = sum(numbers) / len(numbers)
    return highest, lowest, average

marks = [83, 91, 76, 88, 55]
high, low, avg = get_stats(marks)

print(f"Highest: {high}")
print(f"Lowest : {low}")
print(f"Average: {avg:.2f}")

