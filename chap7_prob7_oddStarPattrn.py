n=20
for i in range(n):
    for j in range(2*n-1):
        if j>=n-1-i and j<=n-1+i:
            print("*",end='')
        else:
            print(" ",end='')
    print("\n",end='')