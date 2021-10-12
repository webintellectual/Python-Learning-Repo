import random
a = random.randint(0,100)
print("Guess the number")
count =0
while(1):
    b = int(input())
    if a == b:
        print("victory")
        print(f"You did it in {count+1} attempts\n")
        break
    elif a > b:
        print("try again")
        print(f"Actual number is greater than {b}")
        count+=1
    else:
        print("try again")
        print(f"Actual number is less than {b}")
        count+=1