import sys

N,M = map(int, input().split())
packs = []
ones = []
for _ in range(M):
    pack, one = map(int, input().split())
    packs.append(pack)
    ones.append(one)

min_pack = min(packs)
min_one = min(ones)

num_pack = N//6 #필요 개수 / 6 의 몫
num_one = N%6 #필요개수/ 6 의 나머지 


if min_one*6 < min_pack :  #낱개로만 구매 
    price = N * min_one
elif min_pack < (min_one*num_one) and num_one >0 : #팩으로만 구매 
    price = (num_pack+1) * min_pack
else: 
    price = num_one * min_one + num_pack * min_pack #섞어서 구매 


print(price)