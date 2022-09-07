import math

def jac(arr):
    x = arr[0]
    y = arr[1]
    tl = (1/((math.pow((2-x),2))*(2-y))) - 1
    tr = (1/((2-x)*(math.pow((2-y),2))))
    bl = (4/((math.pow((3-2*x),2))*(3-y)))
    br = (2/((3-2*x)*(math.pow((3-y),2)))) - 1
    return [[tl,tr],[bl,br]]

def func(arr):
    x = arr[0]
    y = arr[1]
    x = (1/(2-x)*(2-y)) -x
    y = (1/(3-2*x)*(3-y)) -y
    return[x,y]

def inverse(j):
    det = ((j[0][0])*(j[1][1])) - ((j[0][1])*(j[1][0])) #ad-bc
    temp = j[0][0]
    j[0][0] = j[1][1] *(1/det)
    j[1][1] = temp *(1/det)
    j[0][1] = - (j[0][1] *(1/det))
    j[1][0] = - (j[1][0] *(1/det))
    return j


def matmult(j, f):
    return [j[0][0]*f[0] + j[0][1]*f[1], j[1][0]*f[0] + j[1][1]*f[1]]

def matsub(arr1, arr2):
    return [(arr1[0] - arr2[0]) , (arr1[1] - arr2[1])]

def newtons(x0):
    n = 0
    x = x0
    while(n < 10000):
        j = inverse(jac(x))
        f = func(x)
        xdelt = matmult(j,f)
        x = matsub(x,xdelt)
        n = n+1
    return x

print(newtons([0,0]))
'''
converging to [1.4999437461503373, 1.9998618080305426]
'''
