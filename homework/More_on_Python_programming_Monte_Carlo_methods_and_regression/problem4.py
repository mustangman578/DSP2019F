import numpy as np
import random as r
import math as m
import matplotlib.pyplot as plt

trials = [i for i in range(1,100000)]

pi = []

def getPi(trials, hits = 0):
    for i in range(int(trials)):
        x2 = r.random()**2
        y2 = r.random()**2
        
        if x2+y2 < 1.0:
            hits += 1
    return float(hits)
    
for i in trials:
    pi.append(4*(getPi(i)/i))
    
plt.semilogx(trials,pi)
plt.ylim(2.6,4)
plt.show
    
