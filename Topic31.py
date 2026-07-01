student = {
    "name"  : "Ankita",
    "age"   : 20,
    "city"  : "Dankuni",
    "marks" : 83.5
}

# Get all keys
print(student.keys())
# dict_keys(['name', 'age', 'city', 'marks'])

# Get all values
print(student.values())
# dict_values(['Ankita', 20, 'Dankuni', 83.5])

# Get all key-value pairs
print(student.items())
# dict_items([('name', 'Ankita'), ('age', 20)...])

# Check if key exists
print("name" in student)     # True
print("phone" in student)    # False

# Total number of keys
print(len(student))          # 4

# Clear everything
student.clear()
print(student)               # {}