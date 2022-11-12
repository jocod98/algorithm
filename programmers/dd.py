from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
dic = dict()
graph = [set([]) for i in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
    
print(graph)
        

q= deque([1])
cnt = 0
visited = [1]

while q :
    a = q.popleft()
    
    for i in graph[a]:
        if i not in visited:
            q.append(i)
            visited.append(i)
            cnt +=1
        else:
            pass
print(cnt)
    



        