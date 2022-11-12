import sys
input = sys.stdin.readline

n = int(input())

prime = [2]


if n ==1 :
    print()

p = 2
while True:
    p+=1 
    flag= 0 
    for i in prime:
        if p%i == 0:
           flag = 1
    if flag == 0 :
        prime.append(p)
        if p>=n and str(p) == str(p)[-1::-1]:
            print(p)
            break
         
