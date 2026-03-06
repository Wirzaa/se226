steps = 0
temp = 0
x = int(input("Enter an integer greater than 9: "))
print(x, end="")
while(x > 9):
    temp = x%10 + (x//10)%10 + (x//100)%10
    steps += 1
    print(" --> ", temp , end="")
    x = temp
print("")
print("Final value: ", x)
print("Total steps: ", steps)
