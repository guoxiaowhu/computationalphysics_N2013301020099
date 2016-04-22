"""
Attractor of Physical Pendulum
Updated on 4/21/2016
Author:GUO Xiao
2013301020099
SI unit
"""
import numpy as np
from pylab import *
from math import *

theta=[]
w=[]#omega
t=[]

"""
input
"""
#parameter
g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
l=1 #(m)
theta0=0 #pi*float(input('theta0(degree)='))/180
theta.append(theta0)
w0=0 #float(input('omega0(rad/s)='))
w.append(w0)
F_D=7.4 #float(input('F_D='))
Omega_D=2 #float(input('Omega_D='))
q=1 #float(input('q='))
t.append(0.0)
n=1000
m=100#it can't be too small
time=n*2*pi/Omega_D
dt=time/n/m

'''
calculation
'''
f=open('pp.txt','w')
for i in range(int(time/dt)):
    w.append(w[i]+dt*(-g/l*sin(theta[i])-q*w[i]+F_D*sin(Omega_D*t[i])))
    angle=theta[i]+dt*w[i+1]
    while angle>pi:
        angle=angle-2*pi# keep theta in the range of -pi to pi
    while angle<-pi:
        angle=angle+2*pi# keep theta in the range of -pi to pi
    theta.append(angle)
    t.append(t[i]+dt)
    print t[-1],theta[-1]
    print >> f,t[-1],theta[-1],w[-1]
f.close()
theta_0=[0 for i in range(n)]
w_0=[0 for i in range(n)]

for i in range(len(theta_0)):
    theta_0[i]=theta[m*i]
    w_0[i]=w[m*i]
#Phase diagram
scatter(theta,w,s=1)
#legend(('nonlinear pendulum'),'upper right')
title('phase diagram',fontsize=20)
xlabel('theta(rad)')
ylabel('omega(rad/s)')
savefig('pp phase diagram.png')
show()
#attractor
scatter(theta_0,w_0,s=1)
#legend(('nonlinear pendulum'),'upper right')
title('Attractor',fontsize=20)
xlabel('theta(rad)')
ylabel('omega(rad/s)')
savefig('pp attractor.png')
show()

