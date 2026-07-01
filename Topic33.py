# Nested Dictionaries
# One student
student = {
    "name"  : "Ankita",
    "age"   : 20,
    "marks" : {
        "Maths"   : 88,
        "Physics" : 76,
        "Python"  : 95
    }
}

# Access nested values
print(student["name"])                   # Ankita
print(student["marks"]["Python"])        # 95
print(student["marks"]["Maths"])         # 88

# Multiple students — dictionary of dictionaries
classroom = {
    "student1" : {
        "name"  : "Ankita",
        "marks" : 83
    },
    "student2" : {
        "name"  : "Priya",
        "marks" : 91
    },
    "student3" : {
        "name"  : "Riya",
        "marks" : 76
    }
}

# Access
print(classroom["student1"]["name"])     # Ankita
print(classroom["student2"]["marks"])    # 91

# Loop through all students
for student_id, info in classroom.items():
    print(f"{info['name']} scored {info['marks']}")