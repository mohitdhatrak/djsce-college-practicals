# str
x = "Hello"
print(x)
print(type(x))
print()  # prints on new line only

# int
x = 1200
print(x)
print(type(x))
print()

# float
x = 12.5
print(x)
print(type(x))
print()

# complex
x = 12 + 45j
print(x)
print(type(x))
print()

# list - ordered, mutable, allows duplicate --> like array
x = [12, 12, 13.00, "Hello", 4 + 5j]
print(x)
print(type(x))
print()

# tuple - ordered, immutable, allows duplicate
x = (12 + 7j, "Hello", 12.0, 55, 55)
print(x)
print(type(x))
print()

# range - ordered, immutable
x = range(13)  # last number not included
print(x)
print(type(x))
print("list", list(x))
print("tuple", tuple(x))
print()

# dictionary - unordered, mutable, doesn't allow duplicate keys, allows duplicate values
x = {"x": 12, "y": 13, "z": "hello", "x": 0}  # does not give error takes only one x
print(x)
print(type(x))
print(x.keys())
print(x.values())
print()

# set - unordered, mutable, doesn't allow duplicates
x = {12, 12, 22.3, "Hello", 12j}  # does not give error takes only one 12 value
print(x)
print(type(x))
print()

# boolean
x = True
y = False
print(x)
print(type(x))
print()

# binary - bytes type is immutable, similar to a tuple
x = b"Hello"
print(x)
print(type(x))
print()

# none
x = None
print(x)
print(type(x))
print()

# id method - unique identifier of an object, represents the memory address of the object
x = 100
print(id(x))
print(id(x))
print(type(id(x)))
print()

# arithmetic
x = 10
y = 6
print(x / y)
print(x**y)
print(x // y)
print()

# assignment
x = 70
x /= 7
print(x)  # prints float value, even if no float
x //= 7
print(x)  # prints float value as x was float
x = 2
x **= 7
print(x)
print()

# logical - and, or, not

# identity - used to check if two variables refer to the exact same object in memory
x = 3
y = 7
print(x is y)
print(x is not y)
print()

#  membership - used to test whether a value exists in a sequence
x = {"Hello", 12, "Python", 12.0, 46j}
print("Python" in x)
print("Python" not in x)
print()

# bitwise
x = 10
y = 7
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(~y)
print(x << 2)
print(x >> 2)
print(y << 2)
print(y >> 2)
