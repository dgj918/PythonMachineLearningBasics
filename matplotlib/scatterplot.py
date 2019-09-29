import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

X = pd.read_csv("data.csv", header=None)
X = X.as_matrix()
print(X)