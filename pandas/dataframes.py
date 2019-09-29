import pandas as pd 

X = pd.read_csv("data_2d.csv", header=None)

print(X)
print(X.info(), X.head(2))

m = X.as_matrix()
print(m, type(m))

print(X[0])
print(X.iloc[0], X.loc[0])

print(X[[0,2]])

# all rows where 0 column < 5 boolean
print(X[0] < 5)

# all rows where 0 column < 5
print(X[ X[0] < 5 ])


