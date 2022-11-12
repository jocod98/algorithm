import sys

N,M = map(int, sys.stdin.readline().split())
T = list(map(int,sys.stdin.readline().split()))
start = 0
end = max(T)
result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2 # 중간값
    for i in T:
        if i>mid :
            total += (i-mid)
    if total < M:
        end = mid-1
    else:
        result = mid
        start = mid+1
    

print(result)

