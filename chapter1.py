#This is a program to solve problem 1.5
from pylab import *
N_A=[]
N_B=[]
t=[]
#input
tau=float(input('time constant='))
N_A.append(float(input('Na0=')))
N_B.append(float(input('Nb0=')))
t.append(0)
time=float(input('total time='))
dt=float(input('time step='))

f=open('chapter1.txt','w')
#calculation
for i in range(int(time/dt)):
    N_A.append(N_A[i]+dt/tau*(N_B[i]-N_A[i]))
    N_B.append(N_B[i]+dt/tau*(N_A[i]-N_B[i]))
    t.append(t[i]+dt)
    print t[-1],N_A[-1],N_B[-1]
    print >> f,t[-1],N_A[-1],N_B[-1]
f.close()
#plot
plot(t,N_A,'--',t,N_B)
legend(('N_A','N_B'))
title('problem 1.5',fontsize=20)
xlabel('t/s')
ylabel('N')
savefig('chapter1.png')
show()
























