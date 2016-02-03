
# coding: utf-8

# In[41]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.linspace(0,3,10)
#y0 = np.random.random(10)
y0 = np.sin(2*x0)

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(0,3,101)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[55]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.linspace(-10,10,20)
#y0 = np.random.random(10)
y0 = np.sin(x0)/x0

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(-10,10,101)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()



# In[64]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.linspace(-3,3,16)
#y0 = np.random.random(10)
y0 = x0**2*np.sin(2*x0)

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(-3,3,101)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[65]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.linspace(-2,2,12)
#y0 = np.random.random(10)
y0 = x0**3*np.sin(3*x0)

plt.plot(x0, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(-2,2,101)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x0, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[ ]:



