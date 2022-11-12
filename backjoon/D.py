import sys
n = int(sys.stdin.readline())

for _ in range(n):
    sum = 0 
    word = list(sys.stdin.readline())
    for i in word:
        if i =="(" : sum +=1
        elif i == ")" : sum-=1

        if sum < 0 : print("NO") ; break

    if sum >= 0 : print("YES")