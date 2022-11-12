name = input()
result = 0
min_chg =0
# 최소 변경 횟수
for i in name:
    min_chg += min(ord(i) - ord('A'), ord('Z') - ord(i)+1)

# 최소 이동 횟수
#ZZAADDERFAAA
pos = 1
f_dist = 0
for _ in range(len(name)):
    while(next <len(name) and next != 'A'):
        next = name[i+1]
        f_dist +=1
        