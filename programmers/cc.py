def solution(n, k, command): # x 선택, c 삭제 + 바로아래행선택, z 되돌리기 선택 그대로
    answer = [1 for i in range(n)]
    now = k
    leng = n-1
    last = []
    
    for cmd in command:
        print(now,answer,leng)
        if cmd == 'C':
            last.append(now)
            answer[now] = 0
            if now == leng:
                now -= 1
            else:
                now += 1
            leng -=1
        elif cmd == 'Z':
            if len(last) > 0 :
                answer[last[-1]] = 1
                last.pop()
                leng += 1
            else:
                pass
        else:
            direction, amount = cmd.split()
            amount = int(amount)
            if direction == 'U':
                if now - amount > 0 :
                    now -= amount
                else:
                    now = 0
            elif direction == 'D':
                if now + amount < leng:
                    now += amount
                else:
                    now = leng
                
    lst = []
    for a in answer:
        if a == 1 :
            lst.append('O')
        else:
            lst.append('X')
               
    return "".join(lst)
    
print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
