'''
solar system
astronomical units
'''

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d
def orbits(x0,y0,v_x0,v_y0):
    v_x=[]
    v_x.append(v_x0)
    x=[]
    x.append(x0)
    v_y=[]
    v_y.append(v_y0)
    y=[]
    y.append(y0)
    r=[]
    r.append(sqrt(x0**2+y0**2))
    time=300
    dt=0.002

    for i in range(int(time/dt)):
        v_x.append(v_x[i]-4*pi**2*x[i]*r[i]**(-3)*dt)
        x.append(x[i]+v_x[i+1]*dt)
        v_y.append(v_y[i]-4*pi**2*y[i]*r[i]**(-3)*dt)
        y.append(y[i]+v_y[i+1]*dt)
        r.append(sqrt(x[i+1]**2+y[i+1]**2))
    return [x,y,v_x,v_y,r]
#Determine the initial value
def initial(a,e):
    x0=a*(1+e)
    y0=0
    v_x0=0
    v_y0=2*pi*sqrt((1-e)/(a*(1+e)))
    return [x0,y0,v_x0,v_y0]

#The orbits of 9 planets
i_M=initial(0.39,0.206)
M=orbits(i_M[0],i_M[1],i_M[2],i_M[3])
x_M=M[0]
y_M=M[1]

i_V=initial(0.72,0.007)
V=orbits(i_V[0],i_V[1],i_V[2],i_V[3])
x_V=V[0]
y_V=V[1]

i_E=initial(1.00,0.017)
E=orbits(i_E[0],i_E[1],i_E[2],i_E[3])
x_E=E[0]
y_E=E[1]

i_Ma=initial(1.52,0.093)
Ma=orbits(i_Ma[0],i_Ma[1],i_Ma[2],i_Ma[3])
x_Ma=Ma[0]
y_Ma=Ma[1]

i_J=initial(5.20,0.048)
J=orbits(i_J[0],i_J[1],i_J[2],i_J[3])
x_J=J[0]
y_J=J[1]

i_S=initial(9.54,0.056)
S=orbits(i_S[0],i_S[1],i_S[2],i_S[3])
x_S=S[0]
y_S=S[1]

i_U=initial(19.19,0.046)
U=orbits(i_U[0],i_U[1],i_U[2],i_U[3])
x_U=U[0]
y_U=U[1]

i_N=initial(30.06,0.010)
N=orbits(i_N[0],i_N[1],i_N[2],i_N[3])
x_N=N[0]
y_N=N[1]

i_P=initial(39.53,0.248)
P=orbits(i_P[0],i_P[1],i_P[2],i_P[3])
x_P=P[0]
y_P=P[1]
#plot
figure(figsize=[16,16])
plot(x_M,y_M,color='grey')
plot(x_V,y_V,color='yellow')
plot(x_E,y_E,color='green')
plot(x_Ma,y_Ma,color='red')
plot(x_J,y_J,color='orange')
plot(x_S,y_S,color='brown')
plot(x_U,y_U,color='blue')
plot(x_N,y_N,color='purple')
plot(x_P,y_P,color='black')
legend(('Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'),'upper left')
title('Orbits of planets in solar system',fontsize=15)
xlabel('x/AU')
xlim(-30,50)
ylabel('y/AU')
ylim(-40,40)
savefig('solar system.png')
show()

