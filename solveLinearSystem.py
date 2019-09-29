import numpy as np 

A = np.array([[1,2], [3,4]])
B = np.array([1,2])

x = np.linalg.inv(A).dot(B)
print(x)
# Always use solve over inverse
x2 = np.linalg.solve(A,B)
print(x2)