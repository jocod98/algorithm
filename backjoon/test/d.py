start, end = map(int,input().split())


lst = []

for i in range(end):
    for j in range(i):
        lst.append(i)
sum=0
for i in range(start-1,end):
    sum += lst[i]
print(sum)