
# coding: utf-8

# In[32]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.random.random(10)
x00 = 3*x0
#y0 = np.random.random(10)
y0 = np.sin(2*x00)

plt.plot(x00, y0, 'o', label='Datos')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x00),max(x00),1000)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x00, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[33]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.random.random(20)
x00 = -10 + 20*x0
#y0 = np.random.random(10)
y0 = np.sin(x00)/x00

plt.plot(x00, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x00),max(x00),1000)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x00, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()



# In[34]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.random.random(16)
x00 = 6*x0 - 3.
#y0 = np.random.random(10)
y0 = x00**2*np.sin(2*x00)

plt.plot(x00, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x00),max(x00),1000)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x00, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[38]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from math import sin

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.random.random(12)
x00 = 4*x0 - 2.
#y0 = np.random.random(10)
y0 = x0**3*np.sin(3*x0)

plt.plot(x00, y0, 'o', label='Data')

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x00),max(x00),1000)


# Available options for interp1d
options = ('linear', 'quadratic', 'cubic')

for o in options:
    f = interp1d(x00, y0, kind=o)    # interpolation function
    plt.plot(x, f(x), label=o)      # plot of interpolated data

plt.legend()
plt.show()


# In[ ]:



