"""
Bifurcation of Physical Pendulum
Updated on 4/21/2016
Author:GUO Xiao
2013301020099
SI unit
"""
import numpy as np
from pylab import *
from math import *

theta_last=[]#list
FD=[]#list

def bifurcation(F_D):
    theta=[]
    w=[]#omega
    t=[]
    g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
    l=1 #(m)
    theta0=0 #pi*float(input('theta0(degree)='))/180
    theta.append(theta0)
    w0=0 #float(input('omega0(rad/s)='))
    w.append(w0)
    Omega_D=2.0 #float(input('Omega_D='))
    q=1 #float(input('q='))
    t.append(0.0)
    n=400
    m=2000#it can't be too small
    time=n*2*pi/Omega_D
    dt=time/n/m
    for i in range(int(time/dt)):
        w.append(w[i]+dt*(-g/l*sin(theta[i])-q*w[i]+F_D*sin(Omega_D*t[i])))
        angle=theta[i]+dt*w[i+1]
        while angle>pi:
            angle=angle-2*pi# keep theta in the range of -pi to pi
        while angle<-pi:
            angle=angle+2*pi# keep theta in the range of -pi to pi
        theta.append(angle)
        t.append(t[i]+dt)

    print theta[-1]
    return theta[-1]

for i in range(1500):
    F_D=6+i*0.001
    FD.append(F_D)
    theta_last.append(bifurcation(F_D))

#Bifurcation diagram
scatter(FD,theta_last,s=1)
title('bifurcation diagram',fontsize=15)
xlabel('F_D')
xlim(6,7.5)
ylabel('theta(rad)')
savefig('bifurcation diagram.png')
show()


