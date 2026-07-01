# Accessing Values
student = {
    "name" : "Anlita",
    "age"  : 20,
    "marks": 83.5
}

print(student["name"])
print(student["age"])
print(student["marks"])

print(student.get("name"))
print(student.get("phone"))
print(student.get("phone", "Not found"))

# Key difference:
print(student["phone"]) # ❌
print(student.get("phone")) # ✅