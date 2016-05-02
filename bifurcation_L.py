"""
Bifurcation of Lorenz Model
Updated on 4/21/2016
Author:GUO Xiao
2013301020099
SI unit
"""
import numpy as np
from pylab import *
from math import *
from Lorenz_1 import *

z_last=[]#list
rr=[]#list

def bifurcation(r):
    z=Lorenz_model(r)[3]
    z_last=z[-1]
    print z[-1]
    return z[-1]

for i in range(2000):
    r=163+i*0.001
    rr.append(r)
    z_last.append(bifurcation(r))

#Bifurcation diagram
scatter(rr,z_last,s=1)
title('bifurcation diagram L',fontsize=15)
xlabel('r')
xlim(163,165)
ylabel('z')
savefig('bifurcation diagram L.png')
show()

