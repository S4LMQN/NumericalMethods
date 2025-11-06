import numpy as np
import math

def derivative_from_limit(func, a, h = 0.001):
    return (func(a + h) - func(a)) / h

def derivative_from_secant(func, a, b):
    return (func(a) - func(b))/(a - b)

print(derivative_from_limit(lambda x: np.e**x, 2))

h = 1
wynik = ["krok", "h","iloraz","poch"]

for k in range(60):
    iloraz = (math.exp(10+h)-math.exp(10))/h
    zapis = [k, h, iloraz, math.exp(10)]
    wynik = np.vstack([wynik, zapis])
    h = h/2

print(wynik)
#np.set_printoptions(precision=10)
#print(np.array(wynik))