def sumOfn(n):
    if n==1:
        return 1
    return n + sumOfn(n-1)
n = int(input("Enter Number: "))
print(sumOfn(n))