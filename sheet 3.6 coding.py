import math

l = 110

def func(x):
    return (math.exp(lamda*(x-1)) - x)

def dervive(x):
    return (lamda*(math.exp(lamda*(x-1))) - 1)

def newtons(x0):
    n = 0
    x = x0
    while(n < 50):
        if(dervive(x) == 0):
            return "Error"
        else:
            x = x - (func(x)/dervive(x))
            n = n+1
    return x

x0 = (1/l)*(math.log(l) - l - 3)

i = 1
while(i<=100):
    lamda = i
    print("lambda = " + str(i) + ":  " + str(newtons(x0)))
    i=i+1
