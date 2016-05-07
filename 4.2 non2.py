'''
solar system
astronomical units
'''

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

#Determine the initial value
def initial(a,e):
    x0=a*(1+e)
    y0=0
    v_x0=0
    v_y0=2*pi*sqrt((1-e)/(a*(1+e)))
    return [x0,y0,v_x0,v_y0]

def orbits(beta):
    i_M=initial(0.39,0.206)
    x0=i_M[0]
    x=[]
    x.append(x0)
    y0=i_M[1]
    y=[]
    y.append(y0)
    v_x0=i_M[2]
    v_x=[]
    v_x.append(v_x0)
    v_y0=i_M[3]
    v_y=[]
    v_y.append(v_y0)
    r=[]
    r.append(sqrt(x0**2+y0**2))
    time=1
    dt=0.001

    for i in range(int(time/dt)):
        v_x.append(v_x[i]-4*pi**2*x[i]/(r[i]**(beta+1))*dt)
        x.append(x[i]+v_x[i+1]*dt)
        v_y.append(v_y[i]-4*pi**2*y[i]/(r[i]**(beta+1))*dt)
        y.append(y[i]+v_y[i+1]*dt)
        r.append(sqrt(x[i+1]**2+y[i+1]**2))
    return [x,y,v_x,v_y,r]

#The orbits of planet

M1=orbits(2.0)
x_M1=M1[0]
y_M1=M1[1]
M2=orbits(2.01)
x_M2=M2[0]
y_M2=M2[1]
M3=orbits(2.1)
x_M3=M3[0]
y_M3=M3[1]
M4=orbits(2.5)
x_M4=M4[0]
y_M4=M4[1]
#plot
figure(figsize=[16,16])

subplot(221)#3 numbers:the total number of rows,columns and the number of subplot
plot(x_M1,y_M1,color='grey')
scatter(0,0,s=1,color='red')
title('beta=2.0',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

subplot(222)
plot(x_M2,y_M2,color='grey')
scatter(0,0,s=1,color='red')
title('beta=2.01',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

subplot(223)
plot(x_M3,y_M3,color='grey')
scatter(0,0,s=1,color='red')
title('beta=2.1',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

subplot(224)
plot(x_M4,y_M4,color='grey')
scatter(0,0,s=1,color='red')
title('beta=2.5',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

savefig('4.2 non-2.png')
show()
