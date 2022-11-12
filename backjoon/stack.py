import sys
n = int(sys.stdin.readline())
st = [] 
for i in range(n):
    order = sys.stdin.readline().split()
    command = order[0]

    if command == "push": 
        num = int(order[-1])
        st.append(num)
    elif command == "pop":
        if len(st) == 0:
            print(-1)
        else: 
            print(st.pop())
    elif command == "size" :
        print(len(st))
    elif command == "empty":
        if len(st) == 0:
            print(1)
        else: print(0)
    elif command == "top":
        if len(st)== 0:
            print(-1)
        else: print(st[-1])