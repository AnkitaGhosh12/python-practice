age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no) : ")
is_member = input("Are you a member? (yes/no) : ")

if age >= 18 and has_id == "yes" and (is_member == "yes" or age >= 21):
    print("Enter allowed")
else:
    print("Enter denied")