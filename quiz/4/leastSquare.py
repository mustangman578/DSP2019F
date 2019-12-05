from scipy.io import loadmat
import scipy.optimize as so
import numpy as np

file = loadmat('Drand.mat')
data = file['Drand']

def getSumDistanceSquared(mean):
    SS = np.sum(data- mean)**2
    return SS

best_fit = so.fmin(leastSquares,x0=10)
best_fit = bestfit[0]
print(best_fit)
