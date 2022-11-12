from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

networks = [[int(x) for x in input().split()] for _ in range(k)]

q = deque([1])
visited = [1]
cnt = 0
while q :
    a = q.popleft()
    
    for net in networks:
        if a == net[0] and net[1] not in visited:
            q.append(net[1])
            visited.append(net[1])
            cnt += 1
            
print(len(visited)-1) 