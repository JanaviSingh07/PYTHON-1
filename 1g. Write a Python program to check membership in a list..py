# Program to check membership in a list

# Define a list
fruits = ["apple", "banana", "cherry", "orange"]

# Read user input
item = input("Enter a fruit name: ")

# Check membership
print("\n--- Membership Check ---")
if item in fruits:
    print(item, "is present in the list.")
else:
    print(item, "is NOT present.")