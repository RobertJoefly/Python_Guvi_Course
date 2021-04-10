def square(n):
    return n*n

numbers = [1,2,3,4,5]

listsquare = map(square, numbers)

print(list(listsquare))
