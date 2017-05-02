#!/usr/bin/python

from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use('Agg')
from matplotlib import colors
from scipy import misc
from matplotlib import animation
import numpy as np
import csv
import matplotlib.pyplot as plt
import random

#at boudary, we assume temperature is 0

#setting
timestep = 1
tottime = 10
xstep = 0.5
alpha = 1

#init initial condition
heatinginit = np.asarray([10,9,8,7,6,5,4,3,5,10])

#init output container
heatmatrix = np.zeros((tottime, len(heatinginit)))
heatmatrix[0] = heatinginit

#print heatmatrix
#print (2 * alpha / (xstep)**2.0) + (1.0 / timestep)

#solving ax = b
for i in xrange(tottime-1):
	#create matrix 'b'
	bmat = heatmatrix[i]
	#create matrix 'a'
	amat = np.zeros((len(heatinginit), len(heatinginit)))
	for j in xrange(len(heatinginit)):
		if j == 0:
			amat[j,0] = (2 * alpha / (xstep)**2.0) + (1.0 / timestep)
			amat[j,1] = -1.0 * (alpha / (xstep)**2.0)
		elif j == (len(heatinginit)-1):
			amat[j, len(heatinginit)-2] = -1.0 * (alpha / (xstep)**2.0)
			amat[j, len(heatinginit)-1] = (2 * alpha / (xstep)**2.0) + (1.0 / timestep)
		else:
			amat[j, j-1] = -1.0 * (alpha / (xstep)**2.0)
			amat[j, j] = (2 * alpha / (xstep)**2.0) + (1.0 / timestep)
			amat[j, j+1] = -1.0 * (alpha / (xstep)**2.0)
	heatmatrix[i+1] = np.linalg.solve(amat, bmat)
print heatmatrix
print [xstep*leng for leng in xrange(len(heatinginit))]

#plotting time
fig = plt.figure()
ax = plt.axes(xlim=(0, xstep*len(heatinginit)), ylim=(0, len(heatinginit)))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
	line.set_data([], [])
	return line,

# animation function.  This is called sequentially
def animate(i):
	x = np.linspace(0, xstep*len(heatinginit), len(heatinginit))
	y = heatmatrix[i]
	line.set_data(x, y)
	return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
           frames=tottime, interval=500, blit=True)
anim.save('/tmp/animation.gif', writer='imagemagick', fps=5)
#plt.show()
