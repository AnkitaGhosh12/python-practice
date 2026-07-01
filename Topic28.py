# Dictionary
# List → access by index number
student = ["Ankita", 20, 83.5]
print(student[0])    # Ankita — but what is index 0? Not clear!

# Dictionary → access by name (much clearer!)
student = {
    "name"  : "Ankita",
    "age"   : 20,
    "marks" : 83.5
}
print(student["name"])    # Ankita — very clear!

#Creating Dictionaries:
empty = {}

student = {
    "name" : "Ankita",
    "age"  : 20,
    "college" : "Canning Government Polytechnic",
    "marks" : 83.5,
    "Passed" : True
}

print(student)