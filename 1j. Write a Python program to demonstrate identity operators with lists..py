# Program to demonstrate identity operators with lists

# Define lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("--- Identity Operators ---")
print("list1 is list2     :", list1 is list2)       # False (different objects, even though values are equal)
print("list1 is list3     :", list1 is list3)       # True (both refer to the same object)
print("list1 is not list2 :", list1 is not list2)   # True (different objects)
print("list1 is not list3 :", list1 is not list3)   # False (same object)

print("\n--- Equality vs Identity ---")
print("list1 == list2     :", list1 == list2)       # True (values are equal)
print("list1 == list3     :", list1 == list3)       # True (values are equal)