x,y = 1,1 #현재 위치 행,열
N = int(input())
P = list(input().split(' '))

xm = [1,0,-1,0] #행
ym = [1,0,-1,0] #열

#R R R U D D

for i in P:
    if (i =='U')& (x>1):
        x+= xm[3]
    if (i =='D')&(x<N):
        x+= xm[0]
    if (i == 'R') & (y<N):
        y += ym[0]
    if (i == 'L') & (y>N):
        y += ym[3]
    else: pass

print(x,y,sep = ' ')