#Define the letters matrice
G=[[' ' for i in range (5)]for j in range (5)] #blank matrix
for i in [1,2,3]:
    G[0][i]='#'
for i in [0]:
    G[1][i]='#'
for i in [0,2,3,4]:
    G[2][i]='#'
for i in [0,3,4]:
    G[3][i]='#'
for i in [1,2,4]:
    G[4][i]='#'

U=[[' ' for i in range (5)]for j in range (5)] #blank matrix
for i in range(4):
    for j in [0,4]:
        U[i][j]='#'
for i in [1,2,3]:
    U[4][i]='#'

O=[[' ' for i in range (5)]for j in range (5)] #blank matrix
for i in [0,4]:
    for j in [1,2,3]:
        O[i][j]='#'
for i in [1,2,3]:
    for j in [0,4]:
        O[i][j]='#'

OUG=[[' ' for i in range (15)]for j in range (5)] #blank matrix
for j in range(5):
    for i in range(5):
        OUG[i][j]=O[i][j]
        OUG[i][j+5]=U[i][j]
        OUG[i][j+10]=G[i][j]

for i in range(5):
    print '\n'
    for j in range(15):
        print OUG[i][j],

