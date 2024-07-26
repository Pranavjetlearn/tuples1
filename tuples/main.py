fruits = ("apple", "orange", "banana")
print(fruits)

#acces in items
print(fruits[0])
print(fruits[0:2])

for i in fruits:
    print(i)

#unpacking
fruit_1, fruit_2, fruit_3 = fruits
print(fruit_1)

#packing
name = "Pranav"
age = 15
height = 5.9
person_tuple = (name, age, height)
print(person_tuple)

veggies = (1,2,3,4,[5,6])
veggies[4][0] = 9
print(veggies)

numbers = (9, 10, 11, 12)
print(numbers)

numbers = (13, 14, 15, 16)
print(numbers)