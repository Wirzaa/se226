num = int(input("Enter an integer between(inclusive) 3 and 9: "))
for i in range(num+2):
    for j in range(1, i):
        print(j, end="")
    print("")
for k in range(num, 0 , -1):
    for j in range(1, k):
        print(j , end="")
    print("")
