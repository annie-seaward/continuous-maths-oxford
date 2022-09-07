import math
def parity(n):
    if n%2 == 0:
        return "even"
    else:
        return "odd"
k = 1 
error = 1 #arbitrary
maxError = 10**-15

while error >= maxError:
    k = k +1
    numerator = ((math.exp(1)) + (((-1)**(k+1))/(math.exp(1)))) #e +- 1/e
    denomenator = (math.factorial(k+1)) #(k+1)!
    error = numerator/denomenator
    print(error)

print(k-1)  #k-1 as while exits when when greater than and looking for no more than
print(parity(k-1)) #return odd or even for final k

"""results when maxError is 10^-15:
0.3917337312146005
0.12859005290127032
0.019586686560730024
0.00428633509670901
0.0004663496800173815
7.654169815551804e-05
6.477078889130298e-06
8.504633128390893e-07
5.888253535572999e-08
6.442903885144616e-09
3.7745214971621784e-10
3.540057079749789e-11
1.797391189124847e-12
1.4750237832290787e-13
6.608055842370761e-15
4.820339160879343e-16
16
even

so smallest k =16, which is even.
"""
