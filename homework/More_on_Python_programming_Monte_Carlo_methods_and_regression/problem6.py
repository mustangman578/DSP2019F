import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(0.0, 14, 0.1)
print(x1)

def f(x):
    return ((x + 1)/12)*(np.exp(-((x-1)**2)/(2*x)))

plt.plot(f(x1))

x = np.random.uniform(0,140,1000)
y = np.random.uniform(0,0.2,1000)

x_inside = []
y_inside = []
x_outside = []
y_outside = []


plt.scatter(x,y,color='red')

plt.show()
