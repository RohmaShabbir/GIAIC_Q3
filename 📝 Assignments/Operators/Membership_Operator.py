# in (Membership)
# not in (Not membership)

# List example
x = [1, 2, 3, 4, 5]

print(3 in x) # Output: True
print(6 in x) # Output: False
print(6 not in x) # Output: True

# String example
text = "Hello, Python!"

print("Python" in text) # Output: True
print("Java" in text) # Output: False
print("Java" not in text) # Output: True

# Dictionary example
data = {
    "name": "Rohma",
    "class": "GIAIC"
}

print("name" in data) # Output: True
print("Rohma" in data) # Output: False
print("class" not in data) # Output: False

# Practice Question

numbers = [10, 20, 30, 40, 50]
print(20 in numbers) 

text = "Python Programming"
print("python" not in text)

info = {
    "course": "AI",
    "duration": "1 Year"
}
print("AI" in info)