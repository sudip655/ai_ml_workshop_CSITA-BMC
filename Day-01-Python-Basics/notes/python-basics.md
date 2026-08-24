# Python Basics (A to Z) - Day 1

This file is a complete Day 1 Python foundation guide.
Use it as notes and as a quick reference while practicing.

## 1. What Is Python?

- Python is a high-level, readable programming language.
- It is used in web development, automation, data science, AI/ML, and more.
- Python uses indentation (spaces) to define blocks of code.

## 2. First Program

```python
print("Hello, World!")
```

## 3. Variables and Data Types

```python
name = "Acer"          # str
age = 21               # int
height = 5.8           # float
is_student = True      # bool

print(name, age, height, is_student)
```

### Type checking

```python
print(type(name))
print(type(age))
```

## 4. Input and Output

```python
user_name = input("Enter your name: ")
print("Welcome,", user_name)
```

## 5. Type Casting

```python
x = "10"
print(int(x) + 5)      # 15

y = 3
print(float(y))        # 3.0
```

## 6. Operators

### Arithmetic

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### Comparison

```python
print(5 > 2)   # True
print(5 == 2)  # False
```

### Logical

```python
print(True and False)
print(True or False)
print(not True)
```

## 7. Conditional Statements

```python
marks = 75

if marks >= 90:
	print("Grade A")
elif marks >= 70:
	print("Grade B")
else:
	print("Grade C")
```

## 8. Loops

### for loop

```python
for i in range(1, 6):
	print(i)
```

### while loop

```python
count = 1
while count <= 5:
	print(count)
	count += 1
```

### break, continue, pass

```python
for i in range(1, 6):
	if i == 3:
		continue
	print(i)
```

## 9. Strings

```python
text = "python"
print(text.upper())
print(text.capitalize())
print(text[0])
print(text[-1])
print(text[0:3])
```

## 10. Lists

```python
nums = [10, 20, 30]
nums.append(40)
nums.remove(20)
print(nums)
```

## 11. Tuples

```python
point = (2, 5)
print(point[0])
```

## 12. Sets

```python
items = {1, 2, 2, 3}
print(items)  # {1, 2, 3}
```

## 13. Dictionaries

```python
student = {
	"name": "Rahul",
	"age": 20,
	"course": "AI"
}

print(student["name"])
student["age"] = 21
```

## 14. Functions

```python
def add(a, b):
	return a + b

result = add(5, 7)
print(result)
```

### Default and keyword arguments

```python
def greet(name, message="Hello"):
	print(message, name)

greet("Acer")
greet("Acer", message="Welcome")
```

## 15. Lambda, map, filter

```python
square = lambda x: x * x
print(square(4))

nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
```

## 16. Modules and Imports

```python
import math
print(math.sqrt(25))

from random import randint
print(randint(1, 10))
```

## 17. File Handling

```python
# write
with open("notes.txt", "w", encoding="utf-8") as f:
	f.write("Python basics complete.\n")

# read
with open("notes.txt", "r", encoding="utf-8") as f:
	print(f.read())
```

## 18. Exception Handling

```python
try:
	n = int(input("Enter number: "))
	print(10 / n)
except ValueError:
	print("Please enter a valid integer.")
except ZeroDivisionError:
	print("Cannot divide by zero.")
finally:
	print("Program ended.")
```

## 19. Object-Oriented Programming (OOP)

```python
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def introduce(self):
		print(f"Hi, I am {self.name} and I am {self.age} years old.")


s1 = Student("Acer", 21)
s1.introduce()
```

### Inheritance

```python
class Animal:
	def sound(self):
		print("Some sound")


class Dog(Animal):
	def sound(self):
		print("Bark")


d = Dog()
d.sound()
```

## 20. List Comprehension

```python
squares = [x * x for x in range(1, 6)]
print(squares)
```

## 21. Useful Built-in Functions

```python
nums = [4, 7, 1, 9]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sorted(nums))
```

## 22. Python for Data/ML Preview

```python
import pandas as pd

data = pd.DataFrame({
	"hours": [1, 2, 3, 4],
	"score": [45, 50, 65, 80]
})
print(data.head())
```

## 23. Practice Tasks (Day 1)

1. Build a calculator using functions.
2. Check if a number is prime.
3. Count vowels in a string.
4. Read a file and count words.
5. Create a Student class with marks and grade method.

## 24. Quick Revision Checklist

- Variables, data types, input/output
- if/elif/else
- for and while loops
- list, tuple, set, dict
- functions and lambda
- file handling and exceptions
- classes and inheritance

You are now ready for Day 2 intermediate Python and problem solving.
