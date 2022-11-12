import sys
lst = []
n = int(input())
ans = []
for i in range(n):
    weight, height = map(int,input().split())
    lst.append([weight,height])

for i in lst:
    rank = 1
    for j in lst:
        if i[0]<j[0] and i[1]<j[1]:
            rank +=1
    ans.append(rank)

for i in ans:
    print(i,end = ' ')