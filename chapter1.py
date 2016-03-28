#This is a program to solve problem 1.5
"""
Updated on Mar 28
Author:GUO Xiao
2013301020099

"""
import numpy as np
from pylab import *
from math import *

N_A=[]
N_B=[]
t=[]
N_A_exact=[]
N_B_exact=[]
#input
tau=float(input('time constant='))
N_A0=float(input('Na0='))
N_A.append(N_A0)
N_B0=float(input('Nb0='))
N_B.append(N_B0)
t.append(0)
time=float(input('total time='))
dt=float(input('time step='))

f=open('chapter1.txt','w')
#calculation and storage
for i in range(int(time/dt)):
    N_A.append(N_A[i]+dt/tau*(N_B[i]-N_A[i]))
    N_B.append(N_B[i]+dt/tau*(N_A[i]-N_B[i]))
    t.append(t[i]+dt)
    print t[-1],N_A[-1],N_B[-1]
    print >> f,t[-1],N_A[-1],N_B[-1]
f.close()

#analytical solution
T=np.linspace(0,time,400,endpoint=True)
for i in range(400):
    N_A_exact.append((N_A0+N_B0+(N_A0-N_B0)*exp(-2*T[i]/tau))/2)
    N_B_exact.append((N_A0+N_B0-(N_A0-N_B0)*exp(-2*T[i]/tau))/2)


#plot and assessment
plot(t,N_A,'--',color='blue')
plot(t,N_B,'--',color='black')
plot(T,N_A_exact,color='blue',linewidth=1.0,linestyle='-')
plot(T,N_B_exact,color='black',linewidth=1.0,linestyle='-')
legend(('N_A(numerical)','N_B(numerical)','N_A(exact)','N_B(exact)'))
title('problem 1.5',fontsize=20)
xlabel('t(s)')
ylabel('N')
xlim(0,10)
ylim(0,100)
savefig('chapter1.png')
show()
























