money=1000 - int(input()) # 낸돈
m_list = [500,100,50,10,5,1]
count = 0
for i in m_list:
    count = count + divmod(money,i)[0]
    money = divmod(money,i)[1]

print(count)