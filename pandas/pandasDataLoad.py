import numpy as np 

x = []

for line in open('data_2d.csv'):
    row = line.split(',')
    sample = list(map(float,row))
    x.append(sample)

print(x)

X = np.array(x)
print(X)