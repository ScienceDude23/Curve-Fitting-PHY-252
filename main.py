import numpy as np
from odrpack import odr_fit
from matplotlib import pyplot as plt

# Load data
data = np.loadtxt("dataset3.csv",
                  delimiter=",",
                  skiprows=1,
                  dtype=float)

# Pull variables and uncertainties
x = data[:,0]
dx = data[:,1]
y = data[:,2]
dy = data[:,3]

# Define weights
weight_x= 1 / (dx**2)
weight_y= 1 / (dy**2)

# Exponential function f(x)=a * (e**(-bx)) + c
def dexp(x,beta):
    a,b,c = beta
    return a * np.exp(-b*x) + c

# Fit the function
result = odr_fit(
    dexp,
    x,
    y,
    beta0=[3.0,0.5,1.5], # Approximate initial parameters
    weight_x=weight_x,
    weight_y=weight_y,
)

a,b,c = result.beta
da,db,dc = result.sd_beta
print("Parameter values: ")
print(a,b,c)
print("Parameter uncertainties: ")
print(da,db,dc)

xfit = np.linspace(min(x),max(x),500) # Even sample of x-values in domain
yfit = dexp(xfit, result.beta) # Plug x-values into regressed function

# Plot the result against the data to validate
plt.scatter(x,y,label="Dataset") # Scatter plot of raw data
plt.plot(xfit,yfit,label="Fitted curve") # Curve with fitted parameters
plt.legend()
plt.savefig("regression.png")