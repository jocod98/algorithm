import sys
word = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
commands = [sys.stdin.readline().strip() for i in range(n)]
word = list(word)
pos = len(word)
for command in commands:
    command = command.split()
    if command[0] == "L":
        if pos != 0:
            pos -=1
            
        else: pass

    elif command[0]== "D":
        if pos < len(word)-1:
            pos +=1
        else: pass

    elif command[0] == "B":
        if pos ==0 : pass
        else:
            word.remove(word[pos-1])
            pos -=1

    elif command[0]== "P":
        word.insert(pos,command[1])
        pos +=1

word = ''.join(word)
print(word)


