
def winner(case):
    case.sort(reverse = True,key = lambda x :x[0])
    #[[5, 5], [4, 1], [3, 2], [2, 3], [1, 4]]
    #len(case) = 5
    count = 0
    for i in range(len(case)):
        flag = 1
        for j in range(i+1,len(case)):
            if case[i][1] > case[j][1]:
                flag = 0
                
                break
        if flag == 1 : 
            count +=1
    return count

case=[]
import sys
n = int(sys.stdin.readline().strip())

#[[[1, 5], [2, 4], [6, 7]], [[1, 4], [2, 4], [1, 6], [2, 4]]]

#풀이

for i in range(n):
    t = int(sys.stdin.readline().strip())
    people = []
    for j in range(t):
        paper, interview = map(int,sys.stdin.readline().split())
        people.append([paper,interview])
    print(winner(people))

