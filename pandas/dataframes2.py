import pandas as pd
from datetime import datetime

X = pd.read_csv('international-airline-passengers.csv', engine='python', skipfooter=3)
print(X)
print(X.columns)

X.columns = ["month", "passengers"]
print(X)
print(X['month'])
print(X.month)

X['ones'] = 1
print(X.head)

d = datetime.strptime('2019-08', '%Y-%m')
print(d)

X['dt'] = X.apply(lambda row:  datetime.strptime(row['month'], '%Y-%m'), axis=1)
print(X.head) 