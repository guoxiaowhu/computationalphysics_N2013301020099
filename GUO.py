#Define the letters matrice
G=[[' ' for i in range (5)]for j in range (5)] #blank matrix
for i in [1,2,3]:
    G[0][i]='#'
G[1][0]='#'
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
# trivial printing way:
print G[0][0],G[0][1],G[0][2],G[0][3],G[0][4],U[0][0],U[0][1],U[0][2],U[0][3],U[0][4],O[0][0],O[0][1],O[0][2],O[0][3],O[0][4]
print G[1][0],G[1][1],G[1][2],G[1][3],G[1][4],U[1][0],U[1][1],U[1][2],U[1][3],U[1][4],O[1][0],O[1][1],O[1][2],O[1][3],O[1][4]
print G[2][0],G[2][1],G[2][2],G[2][3],G[2][4],U[2][0],U[2][1],U[2][2],U[2][3],U[2][4],O[2][0],O[2][1],O[2][2],O[2][3],O[2][4]
print G[3][0],G[3][1],G[3][2],G[3][3],G[3][4],U[3][0],U[3][1],U[3][2],U[3][3],U[3][4],O[3][0],O[3][1],O[3][2],O[3][3],O[3][4]
print G[4][0],G[4][1],G[4][2],G[4][3],G[4][4],U[4][0],U[4][1],U[4][2],U[4][3],U[4][4],O[4][0],O[4][1],O[4][2],O[4][3],O[4][4]

# It will be too trouble to print results by this way,so I print them by following way.

GUO=[[' ' for i in range (15)]for j in range (5)] #blank matrix
for i in range(5):
    for j in range(5):
        GUO[i][j]=G[i][j]
        GUO[i][j+5]=U[i][j]
        GUO[i][j+10]=O[i][j]
for i in range(5):
    print #its function is equal to print'\n'
    for j in range(15):
        print GUO[i][j],#This comma can't be lost

#output to txt file
f=open("GUO.txt",'wb')
for i in range(5):
    f.write('\n')
    for j in range(15):
        f.write(GUO[i][j])
f.close()

#Thanks the instruction from Jing Lei
#More new edition will be published in following days
