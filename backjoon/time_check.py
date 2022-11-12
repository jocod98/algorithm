N = int(input())

#3이 한개부터 5개 

#hour 
if N <3 : 
    n_hour = 0
if N>=3 & N<13:
    n_hour = 1
if N>=13 & N<23:
    n_hour = 2
if N== 23:
    n_hour = 3

# 0000 ~ 5959
#00~ 59 중 3 들어간 숫자 개수 
count = 0 
for i in range(1,60):
    if '3' in str(i):
        count +=1

D_count = (count)^2#5959 까지 3들어간 것 개수

ND_count = 60^2-D_count 

#합은
answer= (N+1) * D_count + ND_count *n_hour
print(answer)



