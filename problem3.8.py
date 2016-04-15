#This is a program to calculate problem 3.8
"""
Nonlinear Pendulum
Updated on 4/15/2016
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
the_lin=[]#theta of linear pendulum
w_lin=[]#omega of linear pendulum

"""
input
"""
#parameter
g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
l=1 #(m)
theta0=pi*float(input('theta0(degree)='))/180
theta.append(theta0)
w0=float(input('omega0(rad/s)='))
w.append(w0)
t.append(0.0)
time=16*pi*sqrt(l/g)
dt=float(input('time step='))
#linear pendulum
the_lin.append(theta0)
w_lin.append(w0)

'''
calculation
'''
f=open('problem3.8.txt','w')
for i in range(int(time/dt)):
    w.append(w[i]+dt*(-g/l*sin(theta[i])))
    theta.append(theta[i]+dt*w[i+1])
    t.append(t[i]+dt)
    w_lin.append(w_lin[i]+dt*(-g/l*the_lin[i]))
    the_lin.append(the_lin[i]+dt*w_lin[i+1])
    print t[-1],theta[-1],the_lin[-1]
    print >> f,t[-1],theta[-1],the_lin[-1]
f.close()
'''
plot 
'''
plot(t,theta,color='blue')
plot(t,the_lin,'--',color='red')
legend(('nonlinear pendulum','linear pendulum'),'lower left')
title('Nonlinear Pendulum and Linear Pendulum',fontsize=20)
xlabel('t(s)')
xlim(0,t[-1])
ylabel('theta(rad)')
savefig('problem3.8.png')
show()
#Phase diagram
plot(w,theta,color='blue')
plot(w_lin,the_lin,'--',color='red')
legend(('nonlinear pendulum','linear pendulum'),'upper right')
title('phase diagram',fontsize=20)
xlabel('omega(rad/s)')
ylabel('theta(rad)')
savefig('problem3.8 phase diagram.png')
show()
