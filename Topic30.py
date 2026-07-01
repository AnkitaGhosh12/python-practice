student = {
    "name"  : "Ankita",
    "age"   : 20,
    "marks" : 83.5
}

# Update existing value
student["marks"] = 90
print(student["marks"])    # 90

# Add new key-value pair
student["city"] = "Dankuni"
student["phone"] = "9876543210"
print(student)

# Delete a key
del student["phone"]
print(student)

# Remove and return value
age = student.pop("age")
print(age)       # 20
print(student)   # age is now removed