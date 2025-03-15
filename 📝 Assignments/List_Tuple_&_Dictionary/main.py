# Lists (Mutable Ordered Collection)

fruits = ["Apple", "Banana", "Mango"]
print(fruits)
print(fruits[1])
print(type(fruits))

fruits.append("orange")
print(fruits)

fruits.remove("Banana")
print(fruits)

# <----------------------->

# Tuples (Immutable Ordered Collection)

colors = ("Red", "Orange", "Green")
print(colors)
print(type(colors))

print(colors[0])  # Accessing element

# colors[1] = "Yellow"  ❌ Error: Tuples can't be modified

# <----------------------->

# Dictionary (Key-Value Pairs)

student = {
    "name" : "Rohma",
    "age" : 20,
    "course" : "Web Development"
}
print(student["name"])
print(type(student))

student["city"] = "Karachi"
print(student)

student["age"] = 21
print(student)

del student["course"]
print(student)






