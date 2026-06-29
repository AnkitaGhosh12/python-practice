fruits = ["apple", "mango", "banana", "orange", "mango"]

# remove() → removes by VALUE (first match)
fruits.remove("mango")
print(fruits)  # ['apple', 'banana', 'orange', 'mango']

# pop() → removes by INDEX (default: last item)
fruits.pop()        # removes last item
print(fruits)       # ['apple', 'banana', 'orange']

fruits.pop(0)       # removes first item
print(fruits)       # ['banana', 'orange']

# clear() → removes everything
fruits.clear()
print(fruits)       # []