import numpy as np
import scipy as sp
from fontTools.misc.bezierTools import epsilon


def heron_sq_root(a, x_0, h = 0.001):
    x_k1 = x_0
    x_k = 0.5 * (x_0 + a/x_0)
    while np.abs(x_k - x_k1) > h:
        x_k1 = x_k
        x_k = 0.5 * (x_k + a / x_k)

    return x_k

def horner(args: list, x: int):
    res = 0
    for item in args:
        if item == args[0]:
            res += item * x
        else:
            res = res * x + item
    return res

def horner_method(poly, c):
    quot = list()
    quot.append(poly[0])

    for i in range(1, len(poly)):
        quot.append(poly[i] + quot[i-1] * c)

    return quot

def e_maclaurin_approx(x, epsilon = 0.001):

    i = 3
    approx = x
    temp = x * x/2

    while temp > epsilon:
        approx = approx + temp
        temp = temp * x/i
        i = i + 1

    return approx + 1

def sine_maclaurin_approx(x = 0, e = 0.001):
    approx = x
    i = 2





