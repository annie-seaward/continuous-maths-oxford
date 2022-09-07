import math

def recur(x1, x, count):
    if(count <= 100):
        x2 = (9/4)*x1 - (1/2)*x
        print(str(count) + ":  " + str(x))
        recur(x2, x1, count+1)

def solved():
    for k in range (1,101):
        x = (4/3)*(math.pow((1/4), float(k)))
        print(str(k) + ":  " + str(x))
        

recur((1/12), (1/3), 1)
solved()
