'''
White dwarf stars:Fermi gas model
Author:GUO Xiao
2013301020099
differential equations:
dp/dr=-a*p^(1/gamma)*/(r^2)
dm/dr=b*r^2*p^(1/gamma)

'''
import numpy as np
from pylab import *
from math import *

def WD(p0,a,b,gamma):
    dr=0.1
    r=[dr]
    p=[p0]
    m=[0]
    i=0
    #f=open('WD.txt','a')
    while 1:
        p.append(p[i]+(-a*p[i]**(1/gamma)*m[i]/(r[i]**2))*dr)
        if p[-1]<=0:
           break
        m.append(m[i]+(b*r[i]**2*p[i+1]**(1/gamma))*dr)
        r.append(r[i]+dr)
        print r[-1],p[-1],m[-1]
        #print >> f,r[-1],p[-1],m[-1]
        i=i+1
    p.pop(-1)
    #print >> f,'/n'
    #f.close()
    R=r[-1]
    M=m[-1]
    print R,M
    return [R,M,r,p,m]

#nonrelativistic case
WDNR=WD(1e-15,0.05,0.005924,5.0/3.0)
r1=WDNR[2]
p1=WDNR[3]
m1=WDNR[4]
figure(figsize=[16,6])
subplot(121)
plot(r1,p1)
title('p(r)')
xlabel('r/km')
ylabel('p')
text(6e3,0.8e-15,'nonrelativistic case')
subplot(122)
plot(r1,m1)
title('m(r)')
xlabel('r/km')
ylabel('m')
text(2e3,0.3,'nonrelativistic case')
savefig('white dwarf NR.png')
#ultra-relativistic case
WDUR=WD(1e-15,1.473,52.46,4.0/3.0)
r2=WDUR[2]
p2=WDUR[3]
m2=WDUR[4]
figure(figsize=[16,6])
subplot(121)
plot(r2,p2)
title('p(r)')
xlabel('r/km')
ylabel('p')
text(5e3,0.8e-15,'ultra-relativistic case')
subplot(122)
plot(r2,m2)
title('m(r)')
xlabel('r/km')
ylabel('m')
text(2e3,1.2,'ultra-relativistic case')
savefig('white dwarf UR.png')
show()
#arbitrary case
'''
#R-M diagram
RNR=[]
MNR=[]
RUR=[]
MUR=[]
for i in range(1000):
    NR=WD(i*5e-17,0.05,0.005924,5.0/3.0)
    RNR.append(NR[0])
    MNR.append(NR[1])
    UR=WD(i*5e-17,1.473,52.46,4.0/3.0)
    RUR.append(UR[0])
    MUR.append(UR[1])

figure(figsize=[8,8]) 
scatter(MNR,RNR,s=1)
scatter(MUR,RUR,s=1)
xlabel('M(solar mass)')
ylabel('R(km)')
legend(('nonrelativistic','ultra-relativistic'),'upper right')
title('R-M diagram')
savefig('White dwarf R-M diagram.png')
show()
'''
