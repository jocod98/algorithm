import sys

lst = [] 
sums =0
n = map(int,sys.stdin.readline().strip())
for _ in range(n):
    rank = map(int,sys.stdin.readline().strip())
    lst.append(rank) 
lst.sort()
idx = list(range(1,n+1,1))

for i in range(n):
    sums+= abs(lst[i]-idx[i])
print(sums)
