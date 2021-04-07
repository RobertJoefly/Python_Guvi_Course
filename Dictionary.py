#unordered, Changeable and Do not allow duplicates

dictt = {
    "Name" : "Robert",    #Key:Value
    "Age" : "25",
    "DOB" : "13-10-1996",
    "Favourites" : ["Billionaire", "private jet", "yatch", "Luxuary Villa"] #we can have list in dictionary
}

print(dictt)
print("**********************************************************************************************")

print("Type of Dictionary")
print(type(dictt))
print("**********************************************************************************************")

print("length of Dictionary")
print(len(dictt))
print("**********************************************************************************************")


print("Access the value of particular key in dictionary")
x = dictt["Name"]
print(x)
#another way to print values
y = dictt.get("Age")
print(y)
print("**********************************************************************************************")

print("Replace the value of particular key")
dictt["Name"] = "Robert Joefly"
print(dictt)
#another way to change the value
dictt.update({"Age":"Twenty Five"})
print(dictt)
print("**********************************************************************************************")

print("Add the new key and value in Dictionary")
dictt["Goal"] = ["Billionaire", "private jet", "yatch", "Luxuary Villa"]
print(dictt)
print("**********************************************************************************************")

print("Remove the key and value from dictionary")
dictt.pop("Favourites")
print(dictt)
print("**********************************************************************************************")

