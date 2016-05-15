'''
Resonance 
astronomical units

'''

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

#Determine the initial value
def initial(a,e):
    x0=a*(1+e)
    v_y0=2*pi*sqrt((1-e)/(a*(1+e)))
    return [x0,v_y0]

def orbits(x_e0,v_ey0):
    m_j=316.7
    m_s=333333.3
#
    x_e=[]
    x_e.append(x_e0)
    
    v_ex0=0
    v_ex=[]
    v_ex.append(v_ex0)

    y_e0=0
    y_e=[]
    y_e.append(y_e0)
    

    v_ey=[]
    v_ey.append(v_ey0)
#Jupiter
    x_j0=initial(5.2,0.048)[0]
    x_j=[]
    x_j.append(x_j0)
    
    v_jx0=0
    v_jx=[]
    v_jx.append(v_jx0)

    y_j0=0
    y_j=[]
    y_j.append(y_j0)
    
    v_jy0=initial(5.2,0.048)[1]
    v_jy=[]
    v_jy.append(v_jy0)

#r
    r_es=[]
    r_es.append(sqrt((x_e0)**2+(y_e0)**2))
    r_js=[]
    r_js.append(sqrt((x_j0)**2+(y_j0)**2))
    r_ej=[]
    r_ej.append(sqrt((x_e0-x_j0)**2+(y_e0-y_j0)**2))

    t=[]
    t.append(0)
    time=40.0
    dt=0.001

    
    for i in range(int(time/dt)):
#asteroid
        v_ex.append(v_ex[i]+dt*(4*pi**2*(-x_e[i])/(r_es[i]**3)+4*pi**2*m_j/m_s*(x_j[i]-x_e[i])/(r_ej[i]**3)))
        x_e.append(x_e[i]+v_ex[i+1]*dt)
        v_ey.append(v_ey[i]+dt*(4*pi**2*(-y_e[i])/(r_es[i]**3)+4*pi**2*m_j/m_s*(y_j[i]-y_e[i])/(r_ej[i]**3)))
        y_e.append(y_e[i]+v_ey[i+1]*dt)
#Jupiter
        v_jx.append(v_jx[i]+dt*(4*pi**2*(-x_j[i])/(r_js[i]**3)))
        x_j.append(x_j[i]+v_jx[i+1]*dt)
        v_jy.append(v_jy[i]+dt*(4*pi**2*(-y_j[i])/(r_js[i]**3)))
        y_j.append(y_j[i]+v_jy[i+1]*dt)

        r_es.append(sqrt((x_e[i+1])**2+(y_e[i+1])**2))
        r_js.append(sqrt((x_j[i+1])**2+(y_j[i+1])**2))
        r_ej.append(sqrt((x_e[i+1]-x_j[i+1])**2+(y_e[i+1]-y_j[i+1])**2))

        t.append(t[i]+dt)
    return [x_e,y_e,x_j,y_j,t]

thr=orbits(3.276,3.471)
x_e=thr[0]
y_e=thr[1]
x_j=thr[2]
y_j=thr[3]
t=thr[4]

#plot
figure(figsize=[8,8])
scatter(x_e,y_e,s=1,color='blue')
plot(x_j,y_j,color='orange')

legend(('Asteroid','Jupiter'),'upper left')
title('astereoids in the gap',fontsize=15)
xlabel('x/AU')
xlim(-4,4)
ylabel('y/AU')
ylim(-4,4)
savefig('asteriod.png')
show()
#3D plot
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_e,y_e,t,color='blue')
ax.plot(x_j,y_j,t,color='orange')
legend(('Asteroid','Jupiter'),'upper left')
ax.set_xlabel('x/AU')
ax.set_ylabel('y/AU')
ax.set_zlabel('t/yr')
savefig('asteriod 3D.png')
show()
