import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

Data = pd.read_csv("points.txt")
Point = np.array([Data.x,Data.y])
Points = np.array(np.transpose([Data.x,Data.y]))


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
    '''
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
              '''
    return BoundingEllipsoidVolume


def twoPointsArray(Point):
    initialVolume = getMinVolPartition(Point)
    firstPointsArray = []
    secondPointsArray = []
    overAllSumOfVolumes = 0
    sumOfVolumes = 0
    clusterID = 0
    while clusterID < 2:
            # Need to step through matching array and find clusterId equal to varible cluster Id (third element)
            x_values = []
            y_values = []
            
            x_first = []
            y_first = []
            x_second = []
            y_second = []
            
            x = Point[0,:]
            y = Point[1,:]
            
            # Need to pass points into clustering algorithm to find volume of child ellipsoids
            PointClusterID = KMeans ( n_clusters = 2 \
                            , random_state = 344 \
                            , init = "k-means++" \
                            , n_init = 100 \
                            , max_iter = 300 \
                            , tol = 0.001 \
                            ).fit_predict(Points)

            pointsArray = [i for i in zip(x,y)]
            matchingArray = [i for i in zip(pointsArray,PointClusterID)]


            for i in matchingArray:
                newClusterID = i[1]
                if newClusterID == clusterID:
                    x_values.append(i[0][0])
                    y_values.append(i[0][1])
                if newClusterID == 0:
                    x_first.append(i[0][0])
                    y_first.append(i[0][1])
                elif newClusterID == 1:
                    x_second.append(i[0][0])
                    y_second.append(i[0][1])

            newPointsArray = np.array([x_values,y_values])
            firstPointsArray = np.array([x_first,y_first])
            secondPointsArray = np.array([x_second,y_second])
            
            print(len(x_first))
            if len(x_first) >= 3:
                # The problem is summing up the volumes 
                sumOfVolumes += getMinVolPartition(newPointsArray)
            else:
                return sumOfVolumes
            

            clusterID += 1
    
    if initialVolume > sumOfVolumes:
        return twoPointsArray(firstPointsArray) + twoPointsArray(secondPointsArray)
    else:
        return sumOfVolumes

print("Final Sum = " + str(twoPointsArray(Point)))
    
    
    
    
'''
def ellispeArea(Point):
    initialVolume = getMinVolPartition(Point)
    
    x = Point[0,:]
    y = Point[1,:]
    
    n_clusters = 2

    
    sumOfVolumes = 0
    numChildren = 2
    
    while initialVolume > sumOfVolumes:

        # Need to pass points into clustering algorithm to find volume of child ellipsoids
        PointClusterID = KMeans ( n_clusters \
                        , random_state = 344 \
                        , init = "k-means++" \
                        , n_init = 100 \
                        , max_iter = 300 \
                        , tol = 0.001 \
                        ).fit_predict(Points)

        pointsArray = [i for i in zip(x,y)]
        matchingArray = [i for i in zip(pointsArray,PointClusterID)]
        #print(matchingArray)

        clusterID = 0
        
        firstEllipsoid = []
        secondEllipsoid = []
        arrayOfPointArrays = []
        
        while clusterID < 2:
            # Need to step through matching array and find clusterId equal to varible cluster Id (third element)
            x_values = []
            y_values = []
            
            x_first = []
            y_first = []
            x_second = []
            y_second = []


            for i in matchingArray:
                newClusterID = i[1]
                if newClusterID == clusterID:
                    x_values.append(i[0][0])
                    y_values.append(i[0][1])
                if newClusterID == 0:
                    x_first.append(i[0][0])
                    y_first.append(i[0][1])
                elif newClusterID == 1:
                    x_second.append(i[0][0])
                    y_second.append(i[0][1])

            newPointsArray = np.array([x_values,y_values])
            firstPointsArray = np.array([x_first,y_first])
            secondPointsArray = np.array([x_second,y_second])
            arrayOfPointArrays.append(firstPointsArray)
            arrayOfPointArrays.append(secondPointsArray)
            
            ellispeArea
            

            sumOfVolumes += getMinVolPartition(newPointsArray)


            clusterID += 1
        
        
            
        
        
        
        numChildren = numChildren**2
        
'''       
        
        
        
        
        
        
        
        
        
        
        
        
        
'''
        while clusterID < n_clusters:
            # Need to step through matching array and find clusterId equal to varible cluster Id (third element)
            x_values = []
            y_values = []


            for i in matchingArray:
                newClusterID = i[1]
                if newClusterID == clusterID:
                    x_values.append(i[0][0])
                    y_values.append(i[0][1])

            newPointsArray = np.array([x_values,y_values])

            sumOfVolumes += getMinVolPartition(newPointsArray)


            clusterID += 1


        n_clusters += 1
        print(n_clusters)
        
        print(sumOfVolumes)
    print(sumOfVolumes)
'''    
