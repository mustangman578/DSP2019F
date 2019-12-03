def integratePDF(nsim):
    import numpy as np
    from numpy.random import random as rand
    from scipy.stats import norm
    Width = 10.
    Height = 0.5
    X = (rand(nsim)-0.5) * 2 * Width
    Y = Height * rand(nsim)
    return 2 * Width * Height * sum( np.less_equal( Y , norm.pdf(X,-2,1) + norm.pdf(X,2,2) ) ) / nsim
