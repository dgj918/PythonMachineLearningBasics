import numPyEx as util
import numpy as np

def dotProd(a,b):
    dot = 0

    for e,f in zip(a,b):
        dot += e * f

    return dot

def npDot(a,b):
    return np.dot(a,b)

# Calculate magnitude or lenght of vector (x,y)T sqrt(x^2 + y^2)

def magOfVect(a):
    return np.sqrt(np.sum(a*a))


a = np.array([1,2])
b = np.array([2,1]) 

dp = dotProd(a,b)
util.printNumArr(dp, "Dot Prod")

sm = util.numArrSumOfMul(a,b)
util.printNumArr(sm, "sum of multiply")

dot = npDot(a,b)
util.printNumArr(dot, "np built in dot")

maga = magOfVect(a)
util.printNumArr(maga, "mag or lenght of a")

magAlin = np.linalg.norm(a)
util.printNumArr(magAlin, "Built in magnitude")

cosA = npDot(a,b) / (magOfVect(a) * magOfVect(b))
util.printNumArr(cosA, "angle between a and b")

util.printNumArr(np.arccos(cosA), "Angle in radians")