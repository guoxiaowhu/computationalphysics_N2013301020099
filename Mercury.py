'''
The precession of Mercury
astronomical units

F=GMM'/(r^2)*(1+alpha/(r^2))
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

def orbits(alpha):
    global a
    a=0.39
    e=0.206
    i_M=initial(a,e)
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
    t=[]
    t.append(0)
    time=2.0
    dt=0.001

    for i in range(int(time/dt)):
        v_x.append(v_x[i]-4*pi**2*x[i]/(r[i]**3)*(1+alpha/(r[i]**2))*dt)
        x.append(x[i]+v_x[i+1]*dt)
        v_y.append(v_y[i]-4*pi**2*y[i]/(r[i]**3)*(1+alpha/(r[i]**2))*dt)
        y.append(y[i]+v_y[i+1]*dt)
        r.append(sqrt(x[i+1]**2+y[i+1]**2))
        t.append(t[i]+dt)
    return [x,y,v_x,v_y,r,t]

def precession(M):
    x=M[0]
    y=M[1]
    r=M[4]
    t=M[5]
    theta=[]
    xp=[]
    yp=[]
    tp=[]
    for i in range(len(r)-2):
        if (r[i+2]-r[i+1])*(r[i+1]-r[i])<0:#choose the perihelions and aphelions
            if r[i+1]>a:#choose the aphelions
                if y[i+1]/x[i+1]>0:
                    angle=arctan(y[i+1]/x[i+1])
                else:
                    angle=pi+arctan(y[i+1]/x[i+1])
                theta.append(angle)
                xp.append(x[i+1])
                yp.append(y[i+1])
                tp.append(t[i+1])
    print tp,theta
    return [tp,theta,xp,yp]

#The orbits of planet
f=open('precession of  Mercury.txt','w')
M1=orbits(0.01)
x_M1=M1[0]
y_M1=M1[1]
p1=precession(M1)
tp1=p1[0]
theta1=p1[1]
print >> f,'alpha=',0.01
print >> f,'tp1=',tp1,'theta1=',theta1
xp1=p1[2]
yp1=p1[3]

M2=orbits(0.005)
x_M2=M2[0]
y_M2=M2[1]
p2=precession(M2)
tp2=p2[0]
theta2=p2[1]
print >> f,'alpha=',0.005
print >> f,'tp2=',tp2,'theta2=',theta2
xp2=p2[2]
yp2=p2[3]

M3=orbits(0.002)
x_M3=M3[0]
y_M3=M3[1]
p3=precession(M3)
tp3=p3[0]
theta3=p3[1]
print >> f,'alpha=',0.002
print >> f,'tp3=',tp3,'theta3=',theta3
xp3=p3[2]
yp3=p3[3]

M4=orbits(0.001)
x_M4=M4[0]
y_M4=M4[1]
p4=precession(M4)
tp4=p4[0]
theta4=p4[1]
print >> f,'alpha=',0.001
print >> f,'tp4=',tp4,'theta4=',theta4
xp4=p4[2]
yp4=p4[3]

M5=orbits(0.003)
x_M5=M5[0]
y_M5=M5[1]
p5=precession(M5)
tp5=p5[0]
theta5=p5[1]
print >> f,'alpha=',0.003
print >> f,'tp5=',tp5,'theta5=',theta5

M6=orbits(0.0005)
x_M6=M6[0]
y_M6=M6[1]
p6=precession(M6)
tp6=p6[0]
theta6=p6[1]
print >> f,'alpha=',0.0005
print >> f,'tp6=',tp6,'theta6=',theta6

M7=orbits(0.0002)
x_M7=M7[0]
y_M7=M7[1]
p7=precession(M7)
tp7=p7[0]
theta7=p7[1]
print >> f,'alpha=',0.0002
print >> f,'tp7=',tp7,'theta7=',theta7

f.close()
#plot
figure(figsize=[16,16])
subplot(221)#3 numbers:the total number of rows,columns and the number of subplot
plot(x_M1,y_M1,color='black')
scatter(0,0,s=1,color='red')
scatter(xp1,yp1,color='green')
title('alpha=0.01',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

subplot(222)
plot(x_M2,y_M2,color='black')
scatter(0,0,s=1,color='red')
scatter(xp2,yp2,color='green')
title('alpha=0.005',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

subplot(223)
plot(x_M3,y_M3,color='black')
scatter(0,0,s=1,color='red')
scatter(xp3,yp3,color='green')
title('alpha=0.002',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

subplot(224)
plot(x_M4,y_M4,color='black')
scatter(0,0,s=1,color='red')
scatter(xp4,yp4,color='green')
title('alpha=0.001',fontsize=15)
xlabel('x/AU')
xlim(-0.6,0.6)
ylabel('y/AU')
ylim(-0.6,0.6)

savefig('Mercury.png')
show()
