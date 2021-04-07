#Ordered eg: list[0], Changeable and Duplicates
list = ["Robert", "Joefly", 13, 10.0, True, "Robert"]
print("List contains below values")
print(list)
print("*****************************")

print("Length of List")
print(len(list))
print("*****************************")

print("Type of List")
print(type(list))
print("*****************************")

print("Access the particular value in list")
print(list[5])
print("*****************************")

print("access values using range")
print(list[2:4])
print(list[0:])
print(list[:5])
print("*****************************")

print("Replace single value")
list[3] = "October"
print(list)
print("*****************************")

print("Replace Multiple values")
list[4:] = "I am a Billioniare", "RJ"
print(list)
print("*****************************")

print("Insert Function") #Insert fuction will add the value in certain position in the list. it will not remove anything
list.insert(4, "DOGE")
print(list)
print("*****************************")

print("Append Function") #Append function will add the value at end of the list
list.append("10 Billion Dollars Networth")
print(list)
print("*****************************")

print("Remove Function") #Remove function will Remove the value fro the list
list.remove("DOGE")
print(list)
print("*****************************")
