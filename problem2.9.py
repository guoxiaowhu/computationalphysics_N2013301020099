#This is a program to calculate the ballistic trajectory
"""
Finished on 
Author:GUO Xiao
2013301020099

"""
import numpy as np
from pylab import *
from math import *
x=[]
y=[]
z=[]
vx=[]
vy=[]
vz=[]
v=[]
t=[]

"""
input
"""
#parameter
w=2*pi/24/3600 #rotation angular speed of Earth(rad/s)
g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
lat=float(input('latitude(degree,North:+,South:-)='))
theta=pi*lat/180
m=float(input('mass=')
B1=
#parameter of B2
B20=   #initial value
a=
alpha=2.5
T0=

#initial condition
x.append(0.0)
y.append(0.0)
z.append(0.0)
vx0=float(input('vx0='))
vy0=float(input('vy0='))
vz0=float(input('vz0='))
vx.append(vx0)
vy.append(vy0)
vz.append(vz0)
v0=(vx0**2+vy0**2+vz0**2)**(1/2)
v.append(v0)
#total time and step
t.append(0.0)
time=float(input('total time='))
dt=float(input('time step='))

'''
calculation
'''
for i in range(int(time/dt)):
    B2=(1-a*z[i]/T0)**alpha*B20
    vx.append(vx[i]+dt*(-B1/m*vx[i]-B2/m*v[i]*vx[i]-2*w*vz[i]*sin(theta)+2*w*vy[i]*cos(theta)))
    vy.append(vy[i]+dt*(-B1/m*vy[i]-B2/m*v[i]*vy[i]-2*w*vx[i]*cos(theta)))
    vz.append(vz[i]+dt*(-g-B1/m*vz[i]-B2/m*v[i]*vz[i]+2*w*vx[i]*sin(theta)))
    x.append(x[i]+dt*vx[i+1])
    y.append(y[i]+dt*vy[i+1])
    z.append(z[i]+dt*vz[i+1])
    v.append(((vx[i+1])**2+(vy[i+1])**2+(vz[i+1])**2)**(1/2))

# 
plot(x,t,y,t,z,t)
plot3D(x,y,z)


