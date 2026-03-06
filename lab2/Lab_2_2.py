n = int(input("Enter an positive integer between(inclusive) 10 and 100: "))
fCount = 0
bCount = 0
fbCount = 0
while(10 > n or n > 100):
    n = int(input("Please enter an viable input: "))
    
for i in range (1, n+1):
    if(i%7 == 0):
        print(i ," is skipped")
        continue
    elif(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
        fbCount += 1
    elif(i%3 == 0):
        print("Fizz")
        fCount += 1
    elif(i%5 == 0):
        print("Buzz")
        bCount += 1
    else:
        print(i)

print("---Summary---")
print("Fizz count : " , fCount)
print("Buzz count : " , bCount)
print("FizzBuzz count : " , fbCount)