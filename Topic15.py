students = ["Ankita", "Priya", "Riya", "Suman"]

print(students[0])   # Ankita  (first item)
print(students[1])   # Priya
print(students[2])   # Riya
print(students[3])   # Suman  (last item)

# Negative indexing (count from end)
print(students[-1])  # Suman  (last item)
print(students[-2])  # Riya   (second last)

marks = [85, 90, 78, 92, 88, 76]

print(marks[0:3])    # [85, 90, 78]  → index 0,1,2
print(marks[2:5])    # [78, 92, 88]  → index 2,3,4
print(marks[:3])     # [85, 90, 78]  → from start to 2
print(marks[3:])     # [92, 88, 76]  → from 3 to end