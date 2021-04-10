#simple lambda functions using single arguement
x = lambda a : a+20
print("simple lambda functions using single arguement")
print(x(5))

#simple lambda function using multiple arguement
x1 = lambda a,b,c : a+b+c
print("simple lambda function using multiple arguement")
print(x1(10,20,3))

#lambda fucntion inside a function
def func(n):
    return lambda a : a*n

doub = func(2)
trip = func(3)

print("Lambda function inside a function")

print("Doubler : ", doub(11))
print("Tripler : ", trip(11))

