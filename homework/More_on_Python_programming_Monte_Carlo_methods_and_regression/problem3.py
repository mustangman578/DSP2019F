def findMaxValLoc(myList=[]):
    
    if myList is None:
        return True

    max = None

    loc = None

    for i, v in enumerate(myList):
        if max is None or v > max:
            max = v
            loc = i
    return((max,loc))
