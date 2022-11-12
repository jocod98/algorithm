lst = []
count = 0
sum=0
for _ in range(3):
    name, score,grade = input().split()
    lst.append([name,score])

for i in lst:
    if i[0] != 'P':
        count +=1
        sum += float(i[1])

ans = sum/count
print(ans)