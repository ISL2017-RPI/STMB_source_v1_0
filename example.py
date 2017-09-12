import STMBv1_0
import STMBFeatSelector as fs
import numpy as np
import scipy.io 

"""
generate a synthetic dataset, a is the feature matrix, 
and b is the label vector

"""
a = np.random.rand(1700, 25) * 10. 
b = 1. * (np.random.randn(1700, 1) > 0.7)

stmb = fs.STMBFeatSelector()
W = stmb.fit_transform(a, b)

print W.shape
