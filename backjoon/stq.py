import sys

n = int(sys.stdin.readline())

st0 = [int(sys.stdin.readline().strip()) for i in range(1,n+1)] # 만들고자 하는 수열
st1 = [i for i in range(1,n+1)]
st1.reverse() # [8,7,6,5,4,3,2,1] # 쓸 수 있는 수들 
st= [] #넣었다 뺐다 할 리스트 
flag = 0
def push():
    st.append(st1.pop()) # st1에서 가져다가 st에 넣는다. 
def pop1():
    st.pop() # st에서 뺴냄. 선택.

answer = []


for i in st0:
    while(True):
        if len(st) == 0 or st[-1] < i : 
            push()
            answer.append("+")
        elif st[-1]==i : 
            pop1()
            answer.append("-")
            break
        else:
            flag = 1
            break
    
if flag == 1: 
    print("NO")
else: 
    for i in answer:
        print(i)