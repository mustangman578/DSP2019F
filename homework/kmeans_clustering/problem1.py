import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x_points = []
y_points = []
with open('points.txt','r') as fh:
    for line in fh:
        if 'x' in line or 'y' in line:
            continue
        else:
            x = line.split(",")
            x_points.append(float(x[0]))
            y_points.append(float(x[1]))
           
plt.scatter(x_points,y_points)
df = pd.DataFrame({'x': x_points,
                   'y': y_points})

Kmean = KMeans(n_clusters=3)
Kmean.fit(df)
Kmean.cluster_centers_

plt.scatter(x_points,y_points)
plt.scatter(6.95090262, 5.74400685, s=200, c='g', marker='s')
plt.scatter(5.69253573, 6.22699062, s=200, c='r', marker='s')
plt.scatter(9.45722894, 8.66951079, s=200, c='y', marker='s')
plt.show()
