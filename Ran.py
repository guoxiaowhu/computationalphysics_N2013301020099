'''
Random walk 1D
Author: GUO Xiao
2013301020099
'''

import numpy as np

from pylab import *
from math import *
import random

#initialization
def Random_walk():
    x=[0]
    x2=[0]
    global n
    n=100

    for i in range(n):
        dx=random.uniform(-1,1)
        x.append(x[i]+dx)
        x2.append(x[i+1]**2)
    x2=array(x2)
    return [x,x2]
n=100
time=range(n+1)
m=500
x_1=Random_walk()[0]
x_2=Random_walk()[0]
x2=Random_walk()[1]
for i in range(m):
    x2=x2+Random_walk()[1]
x2=x2/(m+1)
time=array(time)

figure(figsize=[16,8])
subplot(121)
plot(time,x_1)
plot(time,x_2)
xlim(0,100)
xlabel('step number(or t)')
#ylim(-10,10)
ylabel('x')
text(20,-5,'random step length')
title('Random walk in one dimension')
subplot(122)
scatter(time,x2,s=1)
plot(time,time/3.0)
xlim(0,100)
xlabel('step number(or t)')
ylim(0,)

ylabel('$<x^2>$')
text(10,30,'random step length')
text(60,20,'$<x^2>=t/3$')
title('Random walk in one dimension')
savefig('Random walk 1D r.png')
show()
