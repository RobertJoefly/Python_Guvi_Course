# print fruits which one has letter "a" from the list in normal way using For loop
fruits = ["apple", "banana", "kiwi", "mango"]
newfruits = []

for i in fruits:
    if "a" in i:
        newfruits.append(i)

print(newfruits)
print("***************************************************************")

# print fruits which one has letter "a" from the list in list comprehension way
newfruits1  = [i for i in fruits if "a" in i]
print("List Comprehension way")
print("-------------------------------------------")
print(newfruits1)
print("***************************************************************")

newfruits2 = [i for i in fruits if i != "banana"]
print("remove the value from list")
print(newfruits2)
print("***************************************************************")

newfruits3 = [i.upper() for i in fruits]
print("change the list values to upper case")
print(newfruits3)
print("***************************************************************")

newfruits4 = [i if i != "banana" else "orange" for i in fruits]
print("Replace the values in list")
print(newfruits4)
print("***************************************************************")
