# Python Operators 

## 1. Arithmetic Operator
Arithmetic operators are used for performing mathematical  calculations on numbers.

| Operator | Name          | Example (x=10, y=5) | Result |
|----------|--------------|-----------------|--------|
| `+`      | Addition     | `x + y`         | `15`   |
| `-`      | Subtraction  | `x - y`         | `5`    |
| `*`      | Multiplication | `x * y`       | `50`   |
| `/`      | Division     | `x / y`         | `2.0`  |
| `//`     | Floor Division | `x // y`      | `2`    |
| `%`      | Modulus      | `x % y`         | `0`    |
| `**`     | Exponentiation | `x ** y`      | `100000` |

---

## 2. Assignment Operators
These operators are used to assign values to variables.

| Operator | Example | Same As |
|----------|---------|---------|
| `=`      | `x = 5` | `x = 5` |
| `+=`     | `x += 3` | `x = x + 3` |
| `-=`     | `x -= 2` | `x = x - 2` |
| `*=`     | `x *= 4` | `x = x * 4` |
| `/=`     | `x /= 2` | `x = x / 2` |
| `//=`    | `x //= 2` | `x = x // 2` |
| `%=`     | `x %= 3` | `x = x % 3` |
| `**=`    | `x **= 2` | `x = x ** 2` |

---

## 3. Comparison Operators
Comparison operators are used to compare two values.

| Operator | Meaning | Example (`x = 10, y = 5`) | Result |
|----------|---------|-----------------|--------|
| `==`     | Equal to | `x == y`       | `False` |
| `!=`     | Not equal to | `x != y`   | `True`  |
| `>`      | Greater than | `x > y`    | `True`  |
| `<`      | Less than | `x < y`      | `False` |
| `>=`     | Greater than or equal to | `x >= y` | `True` |
| `<=`     | Less than or equal to | `x <= y` | `False` |

---

## 4. Logical Operators
Logical operators are used to check multiple conditions.

| Operator | Meaning | Example (`x = 10, y = 5`) | Result |
|----------|---------|-----------------|--------|
| `and`    | Both True? | `(x > 5 and y < 10)` | `True` |
| `or`     | Any one True? | `(x > 5 or y > 10)` | `True` |
| `not`    | Reverse result | `not(x > 5)` | `False` |

---

## 5. Identity Operators
These operators check if two variables refer to the same object.

| Operator | Meaning | Example |
|----------|---------|---------|
| `is`     | Same object? | `x is y` |
| `is not` | Different object? | `x is not y` |

Example:
```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)  # True
print(x is z)  # False
```

---

## 6. Membership Operators
These operators check whether a value exists in a sequence (list, tuple, string).

| Operator | Meaning | Example |
|----------|---------|---------|
| `in`     | Present in sequence? | `2 in [1, 2, 3]` → `True` |
| `not in` | Not present? | `4 not in [1, 2, 3]` → `True` |

Example:
```python
text = "Hello Python"
print("Python" in text)  # True
```

---

## 7. Bitwise Operators
Bitwise operators work on binary numbers.

| Operator | Name | Example (`x=5`, `y=3`) | Result |
|----------|------|-----------------|--------|
| `&`      | AND  | `x & y` → `1`  |
| `|`      | OR   | `x | y` → `7`  |
| `^`      | XOR  | `x ^ y` → `6`  |
| `~`      | NOT  | `~x` → `-6`  |
| `<<`     | Left Shift | `x << 1` → `10` |
| `>>`     | Right Shift | `x >> 1` → `2`  |

Example:
```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print(x & y)  # 1
print(x | y)  # 7
print(x ^ y)  # 6
```

---


