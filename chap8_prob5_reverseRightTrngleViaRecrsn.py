def reverseRtTrngle(n):
    for i in range(1,n+1):
        k = n+1 -i
        while k:
            print("*",end="")
            k = k-1
        print()
n = int(input("Enter n: "))
reverseRtTrngle(n)