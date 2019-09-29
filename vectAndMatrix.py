import numpy as np 

npMatrix = np.array([[1,2], [3,4]])
listList = [[1,2], [3,4]]

print(npMatrix, listList)
print(listList[0][0])
print(npMatrix[0][0])
print(npMatrix[0,0])

mat = np.matrix([[1,2], [3,4]])
print(mat)

npMatrix = npMatrix.T
print(npMatrix, "Tranpose")