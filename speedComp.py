import time
import numpy as np 

a = np.random.randn(100)
b = np.random.randn(100)
T = 1000000


def ListDotProd(a,b):
    dot = 0
    for e,f in zip(a,b):
        dot += e*f

    return dot

start = time.time()
for t in range(T):
    listDot = ListDotProd(a,b)
end = time.time()
listTime = end - start

start2 = time.time()
for t in range(T):
    npDot = a.dot(b)
end2 = time.time()
npTime = end2 - start2

print(start, end, listTime, listDot)
print(start2, end2, npTime, npDot)
print(listTime / npTime)



