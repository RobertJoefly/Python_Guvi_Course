def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        else:
            return True

filtered = filter(prime, range(10))

print("Prime Numbers : ", list(filtered))