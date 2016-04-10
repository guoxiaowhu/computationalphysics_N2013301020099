#This is a program to calculate problem 2.19
"""
Updated on 4/10/2016
Author:GUO Xiao
2013301020099
SI unit
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
xp=[]
yp=[]
zp=[]

"""
input
"""
#parameter
g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
m=0.149 #the mass of ball(kg)
S0=4.1e-4*m 
w=2*pi*float(input('angular speed of the ball(rpm)='))/60 #(rad/s)
#parameter of B2
vd=35 #(m/s)
delta=5 #(m/s)
#initial value
#initial condition
x.append(0.0)
y.append(0.0)
z.append(0.0)
v0=49 #float(input('v0='))#(m/s)
phi=0 #pi*float(input('phi(degree)='))/180
theta=pi/2-pi*float(input('elevation angle(degree)='))/180
vx0=v0*sin(theta)*cos(phi)
vy0=v0*sin(theta)*sin(phi)
vz0=v0*cos(theta)
vx.append(vx0)
vy.append(vy0)
vz.append(vz0)
v.append(v0)
t.append(0.0)
time=float(input('total time='))
dt=float(input('time step='))
#parabola
xp.append(0)
yp.append(0)
zp.append(0)

'''
calculation
'''
f=open('problem2.19.txt','w')
for i in range(int(time/dt)):
    B2=(0.039+0.0058/(1+exp((v[i]-vd)/delta)))*m
    flat=0.5*g*(sin(4*w*t[i])-0.25*sin(8*w*t[i])+0.08*sin(12*w*t[i])-0.025*sin(16*w*t[i]))#Flat/m
    vx.append(vx[i]+dt*(-B2/m*v[i]*vx[i]-S0/m*w*vz[i]-flat*vz[i]/v[i]))
    vy.append(vy[i]+dt*(-B2/m*v[i]*vy[i]))
    vz.append(vz[i]+dt*(-g-B2/m*v[i]*vz[i]+S0/m*w*vx[i]+flat*vx[i]/v[i]))
    x.append(x[i]+dt*vx[i+1])
    y.append(y[i]+dt*vy[i+1])
    z.append(z[i]+dt*vz[i+1])
    v.append(((vx[i+1])**2+(vy[i+1])**2+(vz[i+1])**2)**(1/2))
    t.append(t[i]+dt)
    xp.append(vx0*t[i+1])
    yp.append(vy0*t[i+1])
    zp.append(vz0*t[i+1]-g*t[i+1]**2/2)
    print t[-1],x[-1],y[-1],z[-1]
    print >> f,x[-1],y[-1],z[-1]
f.close()
'''
plot 
'''
plot(x,z,color='blue')
plot(xp,zp,'--',color='blue')
legend(('z-x','z-x parabola'))
title('Problem 2.19 z-x',fontsize=20)
xlabel('x(m)')
ylabel('z(m)')
savefig('problem2.19_x-z.png')
show()

plot(y,z,color='red')
plot(yp,zp,'--',color='red')
legend(('z-y','z-y parabola'))
title('Problem 2.19 z-y',fontsize=20)
xlabel('y(m)')
ylabel('z(m)')
savefig('problem2.19_y-z.png')
