import numpy as np  

zArr = np.zeros(10)
print(zArr)

tenZArr = np.zeros([10,10])
print(tenZArr)

tenOArr = np.ones([10,10])
print(tenOArr)

randNp = np.random.random((10,10))
print(randNp)

gausRand = np.random.randn(10,10)
print(gausRand)

print(gausRand.mean())
print(gausRand.var())