# Program to check membership in a string

# Define a string
sentence = "Python programming is fun and powerful."

# Read user input
word = input("Enter a word to check: ")

print("\n--- Membership Check ---")
# Using 'in'
if word in sentence:
    print(f"'{word}' is present in the string.")
else:
    print(f"'{word}' is NOT present in the string.")

# Using 'not in'
print("\n--- Using 'not in' ---")
if word not in sentence:
    print(f"'{word}' is not in the string.")
else:
    print(f"'{word}' is in the string.")