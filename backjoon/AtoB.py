count = 1
case=[]

while(True):
    a= list(map(int,input().split(' ')))
    if any(a)==0: break
    else: case.append(a)

for i in case:
    result = (i[2]//i[1]) *i[0] + min(i[0],i[2]%i[1]) 
    print("Case%d: %d" %(count,result))
    count +=1
