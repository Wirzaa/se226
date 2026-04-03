total = 0   

def my_factorial(x):
    """this function takes your input and multiplies it  with your value-1 recursively until it reaches to 0. At the end returns first inputs factorial."""
    x = int(x)
    if x > 1:
        return (x * my_factorial(x-1))
    elif x == 1 or x == 0:
        return 1
    elif x < 0:
        return "Cannot factorial negative value."


absolute_calc = lambda x , i: ((x**(2*i))/my_factorial(2*i))
xVal = int(input("Enter valuable x"))
nVal = int(input("Enter valuable n"))

def exp_x(x,n):
    total = 0
    for i in range(n):
        total += absolute_calc(x,i)*((-1)**i)
    
    return total

def my_func(r, n):
    """This function takes r and n variables and while n is not negative calculates r**n then it adds it to a global value
      and then it recalls it self with variables (r,n-1) until n becomes negative."""
    global total
    if(n<0):
        return 0
    total += r**n
    if(n>0):
        my_func(r,n-1)


print(exp_x(xVal,nVal))
my_func(3,3)
print(total)
