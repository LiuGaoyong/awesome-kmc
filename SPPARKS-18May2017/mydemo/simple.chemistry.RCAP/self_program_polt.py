#!/usr/bin/env python3
# Reference: 
#    https://github.com/VlachosGroup/Intro-to-KMC/blob/master/well_mixed/01_intro_to_kmc_michaelis_menten.ipynb
#


# Imports necessary libraries
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import odeint, ode

# Set random seed
np.random.seed(0)

# DPI of plots
dpi = 300.

print("Initial Environment Successfully!")

# Stoichiometric matrix
V = np.array([(-1, 1, 0), (-1, 1, 1), (1, -1, -1), (0, 0, 1)])

# Constants and Initial Conditions
nA = 6.023e23 #Avagadro's number
vol = 1e-15 #volume of system

# Molecule counts
X = np.zeros(4)
X[0] = round(5e-7*nA*vol) # molecules of substrate
X[1] = round(2e-7*nA*vol) # molecules of enzyme

# Reaction constants
c=np.zeros((3,1))
c[0] = 1e6/(nA*vol) #c1
c[1] = 1e-4 #c2
c[2] = 0.1 #c3

# Time values
t = 0
tfinal = 50

# Create an array to store time, # of substrate and # of products
data_ga = np.array([(t, X[0],X[1],X[2], X[3])])

start = time.time()
print('Starting kMC simulations...')

# Run the simulation
# Updates concentrations over timeframes until tfinal is reached
while t < tfinal:
    
    # Determines likelyhood of each reaction to occur
    a = np.zeros((3,1))
    a[0] = c[0]*X[0]*X[1]
    a[1] = c[1]*X[2]
    a[2] = c[2]*X[2]
    asum = np.sum(a)
    # Uses random number to determine which reaction occurs
    j = np.min(np.nonzero(np.random.rand()<np.cumsum(a/asum)))
    # Uses random number to determine time for reaction
    tau = np.log(1/np.random.rand())/asum
    # Updates concentrations and time
    X = X + V[:,j]
    t = t + tau
    #print(t, X[0],X[1],X[2], X[3])
    data_ga = np.append(data_ga, [(t, X[0],X[1],X[2], X[3])], axis = 0)
    
end = time.time()
print('The simulation takes {0:.4f} s'.format(end-start))

# plot the graph
fig_ga = plt.figure()
ax_ga = fig_ga.add_subplot(111)
ax_ga.step(data_ga[:,0],data_ga[:,1],'g-o', markerfacecolor = 'g',
    markeredgecolor = 'g')
ax_ga.step(data_ga[:,0],data_ga[:,2],'r-*', markerfacecolor = 'r',
    markeredgecolor = 'r')
ax_ga.step(data_ga[:,0],data_ga[:,3],'b-*', markerfacecolor = 'b',
    markeredgecolor = 'b')
ax_ga.step(data_ga[:,0],data_ga[:,4],'y-*', markerfacecolor = 'y',
    markeredgecolor = 'y')
ax_ga.set_title('GILLESPIE\'S ALGORITHM')
ax_ga.set_xlabel('Time')
ax_ga.set_ylabel('Molecules');
ax_ga.text(40,240,'Product');
ax_ga.text(40,101,'Catalyst');
ax_ga.text(3,240,'Substrate');
ax_ga.text(41,41,'Intermediate');
ax_ga.text(15,300,'Volume: 1e-15');
ax_ga.text(15,280,'k: 1e6,1e-4,0.1');
ax_ga.text(15,260,'Rxns: R+C=A-P+C');
ax_ga.text(15,240,'X0: 301, 120');
fig_ga.set_dpi(dpi)