from scipy.io import loadmat
import scipy.optimize as so
import numpy as np

file = loadmat('Drand.mat')
data = file['Drand']
for i in data:
    mean = (sum(i)/i)
print(summ)
def getSumDistanceSquared(mean):
    SS = np.sum(data- mean)**2
    return SS

best_fit = so.fmin(leastSquares,10)
