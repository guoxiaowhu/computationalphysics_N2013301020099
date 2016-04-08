#This is a program to solve problem 1.6
"""
Finished on Mar 29
Author:GUO Xiao
2013301020099

"""
import numpy as np
from pylab import *
from math import *

N=[]
t=[]

#input
a=float(input('a='))
b=float(input('b='))
N_0=float(input('N0='))
N.append(N_0)
t.append(0)
time=float(input('total time='))
dt=float(input('time step='))

f=open('problem1.6.txt','w')
#calculation and storage
for i in range(int(time/dt)):
    N.append(N[i]+dt*(a*N[i]-b*(N[i])**2))#Attn:It is'**',not'^'
    t.append(t[i]+dt)
    print t[-1],N[-1]
    print >> f,t[-1],N[-1]
f.close()

#plot 
plot(t,N,'--',color='blue')
legend(('N(numerical)'))
title('Problem 1.6',fontsize=20)
xlabel('t(year)')
ylabel('N')

savefig('problem1.6.png')
show()
