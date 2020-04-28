#!/usr/bin/env python3


# Imports necessary libraries
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

filename = './log.spparks.dat'
data = pd.read_table(filename, sep='\s+')
#print(data)
data_ga = np.array(data.drop(labels=['Step','CPU'], axis=1))
#print(data_ga)

# plot the graph
fig_ga = plt.figure()
ax_ga = fig_ga.add_subplot(111)
ax_ga.step(data_ga[:,0],data_ga[:,1],'g-o', markerfacecolor = 'g', markeredgecolor = 'g')
ax_ga.step(data_ga[:,0],data_ga[:,2],'r-*', markerfacecolor = 'r', markeredgecolor = 'r')
ax_ga.step(data_ga[:,0],data_ga[:,3],'b-*', markerfacecolor = 'b', markeredgecolor = 'b')
ax_ga.step(data_ga[:,0],data_ga[:,4],'y-*', markerfacecolor = 'y', markeredgecolor = 'y')
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
fig_ga.set_dpi(300)