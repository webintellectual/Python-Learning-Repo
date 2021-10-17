lt = [56,82,90,8,120,55,90,25,889,345,890,6]
func = lambda i : i%5==0
filterate = filter(func,lt)
print(list(filterate))