#list is a mutable, ordered , allows duplicates
print("===LIST EXAMPLE===")
fruits = ["apple", "banana", "cherry", "apple"] #allow duplicates
print("original list:", fruits)

#add element
fruits.append("mango")
print(fruits)

#remove element
fruits.remove("banana")
print(fruits)

#access by index
print("first fruit:",fruits[-3])

#list comprehension
upper_fruits=[fruit.upper() for fruit in fruits]
print("upppercase fruits:" , upper_fruits)
