"""Write a Python code to reverse the given integer and print the integer"""
def reverse(x):
    print("Reversed Integer: ")
    reversed = x[::-1]
    print(reversed)


user = input("Enter some integer to make it reversal: ")
reverse(user)