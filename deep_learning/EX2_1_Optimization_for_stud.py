# -*- coding: utf-8 -*-
# use GD to bring X2 and X4
import numpy as np


# square of x
def x2(x):
    return (x * x)


# derivative of x2
def x2_(x):
    return 2 * x


"""## Ex2_1 (a) find the minimums of x^2 using Gradient Descent & Momentum"""

# starting point 
X2 = 10
X2m = 10

lr = .01
lrm = .01
num_of_steps = 8000

for i in range(num_of_steps):
    X2m = lrm * X2m - lr * x2_(X2)
    X2 += X2m
    if i % 1000 == 0:
        print("Step:{} \t X2:{} \t X2m:{} ".format(i, X2, X2m))

# =============================================================================
# Examples for print formatting:
#  
# if i%10000 == 0:
#        print("Step:{} \t X2:{} \t X2m:{} ".format(i,X2, X2m))
#        
# =============================================================================


"""## Ex2_1 (b) find the minimums of x^4 using Gradient Descent & Momentum"""


# x to the power of 4
def x4(x):
    return x ** 4


# derivative of x4
def x4_(x):
    return 4 * (x*x*x)


# starting point
X4 = 10
X4m = 10

lr = .001
lrm = .001
num_of_steps = 1000000

for i in range(num_of_steps):
    X4m = lrm * X4m - lr * x4_(X4)
    X4 += X4m
    if i % 1000 == 0:
        print("Step:{} \t X4:{} \t X4m:{} ".format(i, X4, X4m))

# =============================================================================
# Examples for print formatting:
#  
# if i%10000 == 0:
#        print("Step:{} \t X2:{} \t X2m:{} ".format(i,X2, X2m))
#        
# =============================================================================
