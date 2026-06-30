# Parameters and Arguments
def greet(name):
    print(f"Hello {name}! Welcome!")

greet("Ankita")
greet("Priya")
greet("Riya")

# Multiple parameters:
def student_info(name, age, marks):
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print(f"Marks: {marks}")
    print("-" * 20)

student_info("Ankita", 20, 83)
student_info("Riya", 20, 76)

# Default parameters :
def greet(name, message="Good Morning"):
    print(f"Hello {name}! {message}")

greet("Ankita")
greet("Priya", "Good Evening")
greet("Riya", "Happy Birthday! 🎂🎉")