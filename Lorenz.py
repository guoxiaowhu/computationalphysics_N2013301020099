"""
Lorenz model
Updated on 4/28/2016
Author:GUO Xiao
2013301020099
SI unit
"""
import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d
def Lorenz_model(r):
    x=[]
    y=[]
    z=[]
    t=[]
    sigma=10
    b=8/3
    x0=1 
    x.append(x0)
    y0=0
    y.append(y0)
    z0=0
    z.append(z0)
    t.append(0.0)
    global time
    time=50
    dt=0.0001
    for i in range(int(time/dt)):
        x.append(x[i]+dt*sigma*(y[i]-x[i]))
        y.append(y[i]+dt*(-x[i]*z[i]+r*x[i]-y[i]))
        z.append(z[i]+dt*(x[i]*y[i]-b*z[i]))
        t.append(t[i]+dt)
#    print t[-1],x[-1],y[-1],z[-1]
    return [t,x,y,z]
t=Lorenz_model(5)[0]
x_1=Lorenz_model(5)[1]
y_1=Lorenz_model(5)[2]
z_1=Lorenz_model(5)[3]
x_2=Lorenz_model(10)[1]
y_2=Lorenz_model(10)[2]
z_2=Lorenz_model(10)[3]
x_3=Lorenz_model(25)[1]
y_3=Lorenz_model(25)[2]
z_3=Lorenz_model(25)[3]
#plot
plot(t,z_1,color='blue')
plot(t,z_2,color='green')
plot(t,z_3,color='red')
legend(('r=5','r=10','r=25'),'upper left')
title('Lorenz Model z-t',fontsize=15)
xlabel('t')
xlim(0,time)
ylabel('z')
savefig('Lorenz model.png')
show()
#Phase diagram
scatter(x_1,z_1,s=1,color='blue')
scatter(x_2,z_2,s=1,color='green')
scatter(x_3,z_3,s=1,color='red')
legend(('r=5','r=10','r=25'),'lower left')
title('phase diagram',fontsize=15)
xlabel('x')
ylabel('z')
savefig('Lorenz model phase diagram.png')
show()
#3D phase diagram
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_3,y_3,z_3,s=1,color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
savefig('Lorenz model phase diagram 3D.png')
show()

