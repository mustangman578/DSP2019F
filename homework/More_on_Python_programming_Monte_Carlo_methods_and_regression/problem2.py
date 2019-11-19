def findMaxVal(myList = []):
    if myList is None:
        return True
    
    elif len(myList) == 1:
        return myList[0]
    else:
        maxval = findMaxVal(myList[1:])
        return maxval if maxval > myList[0] else myList[0]
