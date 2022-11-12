import sys
n = int(input())
cnt = 0
for i in range(n):
    t = int(sys.stdin.readline().strip())
    people = []
    papers = []
    interviews = []
    
    for j in range(t):
        paper, interview = map(int,sys.stdin.readline().split())
        people.append([paper,interview])
        interviews.append(interview)


    people.sort(reverse = True, key = lambda x : x[0])
    
    for i in people:
        index = interviews.index(i[1])
        if i[1]< min(interviews[index+1:]):
            cnt +=1
        else: pass
    print(cnt)