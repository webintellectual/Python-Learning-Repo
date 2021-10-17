def openFile(file):
    try:
        with open(file,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{file} not found")

f1 = openFile("1.txt")
f2 = openFile("2.txt")
f3 = openFile("3.txt")