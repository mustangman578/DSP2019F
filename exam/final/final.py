import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


Data = pd.read_csv("points.txt")
clusterIDPoints = np.array(np.transpose([Data.x,Data.y]))
plotPoints = np.array([Data.x,Data.y])

PointClusterID = KMeans ( n_clusters = 3 \
                        , random_state = 344 \
                        , init = "k-means++" \
                        , n_init = 100 \
                        , max_iter = 300 \
                        , tol = 0.001 \
                        ).fit_predict(clusterIDPoints)

fig = plt.figure( figsize=(4.5, 4) \
                , dpi= 100 \
                , facecolor='w' \
                , edgecolor='w' \
                ) # create figure object
ax = fig.add_subplot(1,1,1) # Get the axes instance

ax.plot( plotPoints[0] \
       , plotPoints[1] \
       , 'r.' \
       , markersize = 1 \
       ) # plot with color red, as line

ax.set_xlabel('X')
ax.set_ylabel('Y')
fig.savefig('points.png', dpi=200) # save the figure to an external file
plt.show() # display the figure

def getMinVolPartition(Point):
    import numpy as np
    npoint = len(Point[0,:])
    ndim = len(Point[:,0])
    ncMax = npoint // (ndim + 1) # max number of clusters possible
    BoundingEllipsoidCenter = np.array([np.mean(Point[0,:]),np.mean(Point[1,:])])
    SampleCovMat = np.mat(np.cov(Point))
    SampleInvCovMat = np.mat(np.linalg.inv(SampleCovMat))
    PointNormed = np.mat(np.zeros((ndim,npoint)))
    for idim in range(ndim):
        PointNormed[idim,:] = Point[idim] - BoundingEllipsoidCenter[idim]
    MahalSq = PointNormed.T * SampleInvCovMat * PointNormed
    maxMahalSq = np.max(MahalSq)
    BoundingEllipsoidVolume = np.linalg.det(SampleCovMat) * maxMahalSq**ndim
    BoundingEllipsoidCovMat = SampleCovMat * maxMahalSq
    print(
    """
    nd = {}
    np = {}
    ncMax = {}
    SampleCovMat = {}
    InvCovMat = {}
    max(MahalSq) = {}
    BoundingEllipsoidCenter = {}
    BoundingEllipsoidCovMat = {}
    BoundingEllipsoidVolume = {}
    """.format( ndim
              , npoint
              , ncMax
              , SampleCovMat[:]
              , SampleInvCovMat
              , maxMahalSq
              , BoundingEllipsoidCenter
              , BoundingEllipsoidCovMat
              , BoundingEllipsoidVolume
              ))
    return BoundingEllipsoidVolume

def getEllipseSum(plotPoints,PointClusterID):
    firstVolume = getMinVolPartition(plotPoints)
    clusterIDArray = PointClusterID
    
    return firstVolume,clusterIDArray

getEllipseSum(plotPoints,PointClusterID)
