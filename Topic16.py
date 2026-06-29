fruits = ["apple", "mango", "banana"]

# append() → adds to the END
fruits.append("orange")
print(fruits)  # ['apple', 'mango', 'banana', 'orange']

# insert() → adds at a specific position
fruits.insert(1, "grapes")
print(fruits)  # ['apple', 'grapes', 'mango', 'banana', 'orange']

# extend() → add multiple items at once
fruits.extend(["pineapple", "kiwi"])
print(fruits)  # ['apple', 'grapes', 'mango', 'banana', 'orange', 'pineapple', 'kiwi']