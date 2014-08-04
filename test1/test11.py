__author__ = 'atulkanaujia'

from matplotlib import *
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = linspace(-4*pi, 4*pi,100)
z = linspace(-2,2,100)
r = z**2 + 1
x = r*sin(theta)
y = r*cos(theta)
ax.plot(x,y,z,label='parametric curve')
ax.legend()
plt.show()
