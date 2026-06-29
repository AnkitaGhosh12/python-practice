count = 1

while count <= 5:
    print(f"Count is: {count}")
    count = count + 1

password = "ankita123"
attempt = ""

while attempt != password:
    attempt = input("Enter password: ")
    if attempt != password:
        print("Wrong! Try again")

print("Access granted")