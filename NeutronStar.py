'''
Neutron star:pure neutron Fermi gas model
Author:GUO Xiao
2013301020099
SI units
'''
import numpy as np
from pylab import *
from math import *
global c,m_n,hbar,lam,G,msun
hbar=1.05457e-34
c=2.9792458e8
m_n=1.675e-27
lam=hbar/(m_n*c)#lambda
G=6.67e-11
msun=1.989e30


def p_F(rho):
    pF=hbar*(3*pi**2*rho/m_n)**(1.0/3.0)#1.0! not 1 
    return pF

def Ip(x):
    I=3.0/8.0*(x*sqrt(1+x**2)*(2*x**2/3.0-1)+asinh(x))
    return I

def p_(rho):#pressure  equation of state
    p_id=m_n*c**2/(3*pi**2*lam**3)*Ip(p_F(rho)/(m_n*c))
    return p_id

def NS(rho0):
    dr=10#(m)
    r=[0,dr]
    rho=[rho0,0.9999*rho0]#actually drho=0 at r=0, such that avoid infinite
    p=[p_(rho0),p_(0.9999*rho0)]
    m=[0]
    m.append(m[0]+(4*pi*r[1]**2*rho[1])*dr)
    i=1
    #f=open('NS.txt','a')
    while 1:
        dp_drho=(p[i]-p[i-1])/(rho[i]-rho[i-1])
        print 'dp_drho=',dp_drho
        rho.append(rho[i]-dr/dp_drho*G*(rho[i]*c**2+p[i])*(4*pi*r[i]**3*p[i]+m[i]*c**2)/(r[i]*c**2*(r[i]*c**2-2*m[i]*G)))
        if rho[-1]<=0 :
            break
        p.append(p_(rho[i+1]))
        r.append(r[i]+dr)
        m.append(m[i]+4*pi*r[i+1]**2*rho[i+1]*dr)
        print r[-1],p[-1],m[-1],'rho=',rho[-1]
        i=i+1
    rho.pop(-1)
    #print >> f,'/n'
    r=array(r)/1000.0#km
    m=array(m)/msun
    R=r[-1]
    M=m[-1]
    #print >> f,R,M
    #f.close()
    return [R,M,r,p,m,rho]

#
NS1=NS(1e18)
r=NS1[2]
p=NS1[3]
m=NS1[4]
rho=NS1[5]
figure(figsize=[8,15])
subplot(311)
plot(r,p)
title('p(r) pressure')
xlabel('r/km')
ylabel('p/Pa')
subplot(312)
plot(r,m)
title('m(r) mass')
xlabel('r/km')
ylabel('m(solar mass)')
subplot(313)
plot(r,rho)
title('rho(r) density')
xlabel('r/km')
ylabel('$rho(kg/m^3)$')
savefig('Neutron star .png')
show()

#R-M diagram
RNS=[]
MNS=[]

for i in range(1,500):
    N=NS(i*2e15)
    RNS.append(N[0])
    MNS.append(N[1])

for i in range(1,500):
    N=NS(i*1e18)
    RNS.append(N[0])
    MNS.append(N[1])

figure(figsize=[8,8]) 

plot(RNS,MNS,'-',color='black',linewidth=2)
xlabel('R(km)')
ylabel('M(solar mass)')
xlim(0,)
ylim(0,)
title('M-R diagram of Neutron star')
savefig('Neutron Star R-M diagram .png')
show()

