#This is a program to analyse the error of numerical solution of problem 1.5
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
error_A=[]
error_B=[]
#input
tau=float(input('time constant='))

N_A0=float(input('Na0='))
N_A.append(N_A0)
N_A_exact.append(N_A0)
error_A.append(0)

N_B0=float(input('Nb0='))
N_B.append(N_B0)
N_B_exact.append(N_B0)
error_B.append(0)

t.append(0)
time=float(input('total time='))
dt=float(input('time step='))

f=open('chapter1_error.txt','w')
f.write('error')
#calculation and storage
for i in range(int(time/dt)):
    A=N_A[i]+dt/tau*(N_B[i]-N_A[i])
    N_A.append(A)
    B=N_B[i]+dt/tau*(N_A[i]-N_B[i])
    N_B.append(B)
    t.append(t[i]+dt)
    Ae=(N_A0+N_B0+(N_A0-N_B0)*exp(-2*t[i+1]/tau))/2#Attn:t[i+1]!
    N_A_exact.append(Ae)
    Be=(N_A0+N_B0-(N_A0-N_B0)*exp(-2*t[i+1]/tau))/2
    N_B_exact.append(Be)
    error_A.append(A-Ae)
    error_B.append(B-Be)
    print t[-1],error_A[-1],error_B[-1]
    print >> f,t[-1],error_A[-1],error_B[-1]
f.close()

#plot 
plot(t,error_A,'-',color='blue')
plot(t,error_B,'-',color='black')
legend(('error_A','error_B'))
title('Error analysis',fontsize=20)
xlabel('t(s)')
ylabel('error')
xlim(0,10)
savefig('chapter1_error.png')
show()
























