
import pandas as pd

def confidence_interval(data, confidence=0.95):
    import numpy as np
    import scipy as sp
    import scipy.stats

    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h

#confidence_interval([1,2,3,4,4,4,5,5,5,5,4,4,4,6,7,8])
