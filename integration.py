import numpy as np

def rightRiemannSumIntegral(function, a, b, dt = 0.001):
    s = 0
    i = a
    while i < b:
        s += function(i)*dt
        i += dt
    return s

def leftRiemanSumIntegral(function, a, b, dt = 0.001):
    s = 0
    i = a + dt
    while i < b:
        s += function(i) * dt
        i += dt
    return s


