"""Write a Python code to read an integer in a file e.g 123 and convert it to words
e.g One hundred and twenty three and write the result back to the same file such that
your file will have "123 One hundred and twenty three " in it"""

from num2words import num2words

file = open("sample4.txt", "r")
str = " "
for line in file:
    convert = num2words(line)
    str = convert
file.close()

file = open("sample4.txt", "a")
file.write(" "+str)
file.close()

file = open("sample4.txt", "r")
print(file.read())
file.close()

