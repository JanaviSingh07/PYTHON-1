# SETS
print("\n=== SET EXAMPLE ===")
numbers = {1, 2, 3, 2, 1}
print("Set:",numbers)
numbers.add(4)
numbers.discard(2)
print("Set:",numbers)
# Set operations
evens = {2, 4, 6}
print("Union:",numbers|evens)
print("Intersection:",numbers & evens)