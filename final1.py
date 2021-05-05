
#Get a list of name as an input from the user and make the first letters in caps and print each word as a list

def caps(x):
    print("Made a first letter capitalize: ")
    for items in x:
        capital = items.capitalize()
        lst = []
        lst.append(capital)
        print(lst)

user = list((input("Enter the list of names: ").split()))
print("                                                ")
print("List of names: ", user)
print("                                                ")
caps(user)
