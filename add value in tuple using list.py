#Add values in tuple using list.
x= ("Robert", "Joefly", 13, 10)
print(x)
print(type(x))
print("***************************************************")


# change the tuple to list
print("change the tuple to list")
y = list(x)
print(y)
print(type(y))
print("***************************************************")

#Replace the value in list
print("Replace the value in the list")
y[3] = "October"
print(y)
print("***************************************************")

#change list to tuple
print("Again change the list to tuple")
z = tuple(y)
print(z)
print(type(z))

