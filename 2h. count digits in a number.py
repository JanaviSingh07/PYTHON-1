# Program to count digits in a number

num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10   # remove last digit
        count += 1

print(f"Number of digits: {count}")