import sys
n = int(sys.stdin.readline())
st = []
st1 = [int(sys.stdin.readline().strip()) for _ in range(n)]
st0 =[]
for i in range(1,n+1): st0.append(i)
st0.reverse()
answer = []

for i in st1:
    while(True):
        if len(st) == 0 or st[-1]<i:
            st.append(st0.pop())
            print("+")
        elif st[-1]==i:
            answer.append(st.pop())
            print("-")
            break