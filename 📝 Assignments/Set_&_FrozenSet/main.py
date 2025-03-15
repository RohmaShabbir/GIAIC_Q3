# Set (Mutable, Unordered Collection)
fruits = {"Apple", "Mango", "Banana", "Apple"}
print(fruits)

fruits.add("Orange")
print(fruits)

fruits.remove("Banana")
print(fruits)

fruits.clear()
print(fruits)

# <------------------->

# Frozenset (Immutable Set)
numbers = frozenset([1, 2, 3, 4, 5])
print(numbers)  # frozenset({1, 2, 3, 4, 5})

# numbers.add(6)  ❌ Error: You cannot modify a frozenset.


