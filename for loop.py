#for loop using List
numbers = [1,2,3,4,5,13,23,100]
for x in numbers:
    print(x)
print("**************************************")

#for loop using  string
name = "Robert"
for y in name:
    print(y)
print("**************************************")

#break statement

num = [1,2,3,4,5,13,23,100]
for z in num:
    print(z)
    if z==5:
        break
print("**************************************")

#continue statement

n = [1,2,3,4,5,13,23,100]
for a in n:
    if a==4:
        continue
    print(a)
print("**************************************")

#range function

for b in range(100):
    print(b)
print("**************************************")

for c in range(33, 100):
    print(c)
print("**************************************")
