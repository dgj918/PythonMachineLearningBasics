import matplotlib
matplotlib.use('MacOSX')
matplotlib.rcParams['interactive'] == True

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel("time")
plt.ylabel("Some function of time")
plt.title("My Chart")
plt.show()