import random
def doRandomWalk(nstep,startPosition):
   for i in range(nstep):
       step = random.randint(0,1)
       if step == 1:
           startPosition += 1
       else:
           startPosition -= 1
   return startPosition
def simulateRandomWalk(nsim,nstep,startPosition):
   import matplotlib.pyplot as plt
   finalStep = []
   for i in range(nsim):
       finalStep.append(doRandomWalk(nstep,startPosition))
   plt.hist(finalStep)
   plt.show()
