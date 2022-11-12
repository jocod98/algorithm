import sys

t = int(input())

for i in range(t):
    profit = 0
    count = 0
    case= []
    purch =[]
    n=int(input())
    case = [map(int,sys.stdin.readline().split())for i in range(n)]
    for i in range(n-1):
        if case[i]<=case[i+1]:
            purch.append(case[i])
        elif case[i] > case[i+1]:
            for j in purch:
                profit += case[i+1] - j
            purch = []


