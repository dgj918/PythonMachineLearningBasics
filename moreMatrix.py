import numpy as np
import numPyEx as util

m = np.array([[1,2], [3,4]])
util.printNumArr(m, "matrix")

minv = np.linalg.inv(m)
util.printNumArr(minv, "inverse: ")

util.printNumArr(minv.dot(m), "Identity: ")
util.printNumArr(m.dot(minv))
util.printNumArr(np.linalg.det(m))
util.printNumArr(np.diag(m))
util.printNumArr(np.diag([1,2]), "diagnoal")

a = np.array([1,2])
b = np.array([3,4])

print(np.outer(a,b))
print(np.inner(a,b))

X = np.random.randn(100, 3)

conv = np.cov(X)

print(conv.shape)

print(np.cov(X.T))

print(np.linalg.eigh(conv))