# Without return — only prints, can't reuse:
def add(a, b):
    print(a + b)

result = add(5, 3)
print(result)

# With return — value comes back for reuse:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

print(add(10, 20))
print(add(5, 3) * 2)

# Practical examples:
# Calculate percentage
def percentage(marks, total):
    return (marks / total) * 100

p = percentage(83, 100)
print(f"Your percentage: {p}%")   # 83.0%

# Check pass or fail
def result(marks):
    if marks >= 40:
        return "PASS ✅"
    else:
        return "FAIL ❌"

print(result(83))   # PASS ✅
print(result(35))   # FAIL ❌

# Return multiple values
def student_stats(marks):
    total   = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest  = min(marks)
    return total, average, highest, lowest

marks = [83, 91, 76, 88, 55]
t, avg, h, l = student_stats(marks)
print(f"Total   : {t}")
print(f"Average : {avg}")
print(f"Highest : {h}")
print(f"Lowest  : {l}")