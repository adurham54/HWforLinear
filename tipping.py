from fitting_functions import *
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.stats import norm

data = np.loadtxt("tips.csv", delimiter=",", dtype=str)

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

print_equation(slope, intercept, "dollars","dollars") #The equation of the line is: y= 0.18221473222560391 dollar/dollar + -0.2922674195507699 dollars

fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("Bill (Dollars)") 
plt.ylabel("Tip (Dollars)")  
plt.show()

x = data[1:, 0].astype(np.float32)
y = data[1:, 6].astype(np.float32)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

print_equation(slope, intercept, "dollars","%") #The equation of the line is: y= 0.04881243455874584 %/dollar + 15.509648238069316 %

fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("Bill (Dollars)") 
plt.ylabel("PctTip (%)")  
plt.show()
