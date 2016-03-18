# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pylab as p
from scipy import integrate



b = 0.0 #fricción
g = 9.8 #gravedad
l = 1. #longitud de la cuerda
c = g/l

#condiciones iniciales 
X_f0 = array([ -4*np.pi , 4*np.pi])
X_f1 = array([ -2*np.pi, np.pi*0])
t = np.linspace(0, 20, 300) #rango de tiempo

def pend(y, t, b, c):
     theta, omega = y
     dydt = [omega, -b*omega - c*np.sin(theta)]
     return dydt




# <codecell>


# <codecell>

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pylab as p
from scipy import integrate



b = 0.0 #fricción
g = 9.8 #gravedad
l = 1. #longitud de la cuerda
c = g/l

#condiciones iniciales 
X_f0 = array([ -4*np.pi , 4*np.pi])
X_f1 = array([ -2*np.pi, np.pi*0])
t = np.linspace(0, 20, 300) #rango de tiempo

def pend(y, t, b, c):
     theta, omega = y
     dydt = [omega, -b*omega - c*np.sin(theta)]
     return dydt


values  = linspace(-1, 1, 60)                          # position of X0 between X_f0 and X_f1
vcolors = p.cm.terrain_r(linspace(0.5, 1., len(values)))  # colors for each trajectory
vcolors2 = p.cm.winter_r(linspace(0.5, 1., len(values)))
f2 = p.figure()

#-------------------------------------------------------
# plot trajectories
for v, col in zip(values, vcolors):
    X0 = v * X_f0                               # starting point
    X = integrate.odeint( pend, X0, t, (b, c) )        # we don't need infodict here
    p.plot( X[:,0], X[:,1], lw=3.5*v, color=col, label='X0=(%.f, %.f)' % ( X0[0], X0[1]) )
    
    
    # plot trajectories
for v, col in zip(values, vcolors):
    X0 = v * X_f1                               # starting point
    X = integrate.odeint( pend, X0, t, (b, c) )        # we don't need infodict here
    p.plot( X[:,0], X[:,1], lw=3.5*v, color=col, label='X0=(%.f, %.f)' % ( X0[0], X0[1]) )


#-------------------------------------------------------
# define a grid and compute direction at each point
#ymax = p.ylim(ymin=0)[1]                        # get axis limits
#xmax = p.xlim(xmin=0)[1]
#nb_points   = 20

#x = linspace(0, xmax, nb_points)
#y = linspace(0, ymax, nb_points)

#X1 , Y1  = meshgrid(x, y)                       # create a grid
#DX1, DY1 = pend([X1, Y1])                      # compute growth rate on the gridt
#M = (hypot(DX1, DY1))                           # Norm of the growth rate
#M[ M == 0] = 1.                                 # Avoid zero division errors
#DX1 /= M                                        # Normalize each arrows
#DY1 /= M

#-------------------------------------------------------
# Drow direction fields, using matplotlib 's quiver function
# I choose to plot normalized arrows and to use colors to give information on
# the growth speed
p.title('Espacio fase del pendulo simple.')
#Q = p.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=p.cm.jet)
#p.xlabel('Number of rabbits')
#p.ylabel('Number of foxes')
#p.legend()
p.grid()
p.xlim((-4*np.pi)/2, (4*np.pi)/2)
p.ylim(-4*np.pi, 4*np.pi)
f2.savefig('rabbits_and_foxes_2.png')

# <codecell>


