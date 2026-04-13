# Program to demonstrate identity operators with integers

# Define integers
a = 10
b = 10
c = 20

print("--- Identity Operators ---")
print("a is b     :", a is b)       # True if both refer to the same object
print("a is c     :", a is c)       # False because values differ
print("a is not b :", a is not b)   # False because a and b are the same object
print("a is not c :", a is not c)   # True because a and c are different objects

# Demonstrating with larger integers
x = 1000
y = 1000
print("\n--- Larger Integers ---")
print("x is y     :", x is y)       # May be False (depends on Python's object caching)
print("x == y     :", x == y)       # Always True because values are equal