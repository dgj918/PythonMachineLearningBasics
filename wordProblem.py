"""
The admission for a small fair is 1.50 for children and 4.00 for adults. On a certian day 2200 people
attend the fair and $5050 is collected. How many children and adults attended?

x1 + x2 = 2200
1.5x1 + 4x2 = 5050

1       1   x1  2200
1.5     4   x2  5050
"""
import numpy as np 

x1 = np.array([[1,1], [1.5,4]])
print(x1)
x2 = np.array([2200,5050])
print(x2)

ans = np.linalg.solve(x1,x2)
print(ans)