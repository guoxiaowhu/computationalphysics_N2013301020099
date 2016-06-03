'''
Random walk 3D
Author: GUO Xiao
2013301020099
'''

import numpy as np

from pylab import *
from math import *
import random
import mpl_toolkits.mplot3d

#initialization
def Random_walk():
    x=[0]
    y=[0]
    z=[0]
    r2=[0]
    global n
    n=100

    for i in range(n):
        r_x=random.uniform(0,1)
        r_y=random.uniform(0,1)
        r_z=random.uniform(0,1)
        if r_x<0.5:
            x.append(x[i]+1/sqrt(3))
        else:
            x.append(x[i]-1/sqrt(3))
        if r_y<0.5:
            y.append(y[i]+1/sqrt(3))
        else:
            y.append(y[i]-1/sqrt(3))
        if r_z<0.5:
            z.append(z[i]+1/sqrt(3))
        else:
            z.append(z[i]-1/sqrt(3))
        r2.append(x[i+1]**2+y[i+1]**2+z[i+1]**2)

    r2=array(r2)
    return [x,y,z,r2]
n=100
time=range(n+1)
m=500
Ran=Random_walk()
x=Ran[0]
y=Ran[1]
z=Ran[2]
r2=Ran[3]
for i in range(m):
    r2=r2+Random_walk()[3]
r2=r2/(m+1)
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
title('Random walk in 3 dimension')
savefig('Random walk trajector 3D.png')

figure()
scatter(time,r2,s=1)
plot(time,time)
xlim(0,100)
xlabel('step number')
ylim(0,100)
ylabel('$<x^2>$')
title('Random walk in 3 dimension')
savefig('Random walk 3D.png')
show()

