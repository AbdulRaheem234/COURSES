# Creating an empty set

b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add((4, 5, 6))

# Cannot add list or dictionary to sets
# b.add({4:5})
print(b)

# Prints the length of this sets
print(len(b))
b.remove(5)
print(b)
print(b.pop())
print(b)
