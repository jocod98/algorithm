import sys
n = map(int,sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
size = len(lst)
count = 0
while(True):
    if len(lst) ==0: break
    if len(lst)>= min(lst):
        for i in range(min(lst)):
            lst.pop()
        count +=1
    else:
        break
        
print(count)