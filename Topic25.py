#  Local vs Global Variables
#  Global Variable
name = "Ankita"

def show_name():
    print(name)

show_name()
print(name)

# Local Variable
def greet():
    message = "Hello!"
    print(message)

greet()

# Important Rule — Local variable hides Global with same name:
name = "Ankita"

def greet():
    name = "Priya"
    print(name)

greet()
print(name)

# Using global keyword — to modify global variable inside function:
score = 0
def add_point():
    global score
    score = score + 1

add_point()
add_point()
add_point()
print(score)