# Program to check if a character is a vowel

ch = input("Enter a character: ")

# Convert to lowercase to handle both cases
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("The character is a vowel.")
else:
    print("The character is not a vowel.")