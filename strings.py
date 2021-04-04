a = "Apple"
b = 'Banana'

print(a)
print(b)
print("*****************************************************")

#multi line string

c = """Robert
Joefly"""

d = '''I am
a
Billionaire'''

print(c)
print(d)
print("*****************************************************")

#Position of Character (python doesn't having a character)

e = "Hello World"
print(e[0])
print("*****************************************************")

#looping the string
f = "Robert Joefly"
for i in f:
    print(i)
print("*****************************************************")

#length of string
g = "I am a Billionaire"
print(len(g))
print("*****************************************************")

#checking word in sentence
h = "Robert is a Billionaire"
print("Billionaire" in h)
print("Joefly" in h)
print("*****************************************************")

#slicing the string
j = "Robert Joefly"
print(j[0:3])
print(j[:6])
print(j[0:])
print(j[-6:-3])
print("*****************************************************")

#modify the string
k = "Robert Joefly"
print(k.upper())
print(k.lower())
print("*****************************************************")

#Remove the white spaces
l = "    Robert Joefly     "

print(l)
print(l.strip())
print("*****************************************************")

#Replace the string
print(l.replace("R","r"))
print("*****************************************************")

#split the string
m = "Robert Joefly"
print(m.split(" "))
print("*****************************************************")

#concatenation
n = "Robert"
o = "Joefly"

print(n+o)
print(n+" "+o)
print("*****************************************************")







