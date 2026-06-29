# Day 3 Practice - Ankita's Python Journey

print("=" * 35)
print("      LOOP PRACTICE PROGRAM")
print("=" * 35)

# Part 1 - Multiplication Table
n = int(input("Enter a number for table: "))
print(f"\n--- Multiplication Table of {n} ---")
for i in range(1, 11):
    print(f"  {n} x {i:2} = {n * i}")

# Part 2 - Sum of numbers
print("\n--- Sum Calculator ---")
total = 0
for i in range(1, 11):
    total = total + i
print(f"  Sum of 1 to 10 = {total}")

# Part 3 - Find even numbers
print("\n--- Even Numbers from 1 to 20 ---")
for i in range(1, 21):
    if i % 2 == 0:
        print(f"  {i}", end=" ")
print()

# Part 4 - while loop with break
print("\n--- Guess the Number Game ---")
secret = 7
attempts = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    attempts = attempts + 1

    if guess < secret:
        print("Too low! Try again ⬆️")
    elif guess > secret:
        print("Too high! Try again ⬇️")
    else:
        print(f"Correct! 🎉 You got it in {attempts} attempts!")
        break