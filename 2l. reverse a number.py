# Program to reverse a number

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10        # extract last digit
    rev = rev * 10 + digit  # build reversed number
    num = num // 10         # remove last digit

print(f"Reversed number is: {rev}")