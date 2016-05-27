import numpy as np
import matplotlib.pyplot
from pylab import *
from math import *
import mpl_toolkits.mplot3d

dx=0.01
c=300.0 #speed
dt=dx/c
length=int(1.0/dx)
time=200
k=1000
y=[[0 for i in range(length)]for n in range(time)]#i represents x, n represents t
#initialize
for i in range(length):
    y[0][i]=exp(-k*(i*dx-0.3)**2)
    y[1][i]=exp(-k*(i*dx-0.3)**2)
#for i in range(2*length/5):
#    y[0][i]=3*i*dx
#    y[1][i]=3*i*dx
#for i in range(2*length/5,length):
#    y[0][i]=2-2*i*dx
#    y[1][i]=2-2*i*dx

#plot(range(length),y[1])
#show()

r=c*dt/dx
#iteration
for n in range(time-2):
    for i in range(1,length-1):
        y[n+2][i]=2*(1-r**2)*y[n+1][i]-y[n][i]+r**2*(y[n+1][i+1]+y[n+1][i-1])
y=array(y)
add=array([1 for i in range(length)])
for n in range(0,time,20):
    yp=y[n]+add*n/20
    plot(range(length),yp)
#xlim(-1,1)
xlabel('x')
#ylim(-1,1)
ylabel('y and t')
title('Waves on a string (fixed ends)')
#text(0,2,'reflection and inversion')#'$F_D$'
#savefig('wave 6.4.png')
savefig('wave 6.2.png')
#savefig('wave .png')
figure()
y5=[]
t=array(range(time))*dt
for n in range(time):
    y5.append(y[n][5])
plot(t,y5)
xlabel('t/s')
ylabel('y/m')
title('vibration of a point on a string')
text(0,0.56,r'a point at 5% of this string')
#savefig('vibration 6.6 pluck.png')
#savefig('vibration 6.6.png')
#savefig('vibration .png')
show()
'''
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V,rstride=1, cstride=1,linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('V')
title('electric potential')
savefig('electric potential J 3D.png')
figure(figsize=[8,8])
Q=quiver(X,Y,Ex,Ey,scale=100)
xlim(-1,1)
xlabel('x')
ylim(-1,1)
ylabel('y')
title('electric field')
savefig('electric field J.png')
show()
'''
