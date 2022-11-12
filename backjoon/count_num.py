import sys
n,x = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
start =0
end = len(lst)-1


while(True):
    mid = (start + end)//2
    if lst[mid]>x : 
        end = mid-1
    elif lst[mid] < x :
        start = mid+1
    else:
        




