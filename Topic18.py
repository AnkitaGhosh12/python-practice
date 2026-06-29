marks = [85, 90, 78, 92, 88, 76]
names = ["Riya", "Ankita", "Priya", "Suman"]

# Length
print(len(marks))        # 6

# Maximum and Minimum
print(max(marks))        # 92
print(min(marks))        # 76

# Sum
print(sum(marks))        # 509

# Sort (ascending)
marks.sort()
print(marks)             # [76, 78, 85, 88, 90, 92]

# Sort (descending)
marks.sort(reverse=True)
print(marks)             # [92, 90, 88, 85, 78, 76]

# Alphabetical sort
names.sort()
print(names)             # ['Ankita', 'Priya', 'Riya', 'Suman']

# Count occurrences
numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2))     # 3

# Find index of item
print(names.index("Priya")) # 1