import numpy as np
from matplotlib import pyplot as plt

# Load data from csv
data = np.loadtxt("dataset3.csv",
                  delimiter=",", 
                  skiprows=1, 
                  dtype=float)

# Pull out variables
x = data[:,0]
y = data[:,2]

# Plot data to get an idea of function shape
plt.plot(x,y)
plt.xlabel("x data")
plt.ylabel("y data")
plt.savefig("dataset3.png")