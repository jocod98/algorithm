import sys
n= int(sys.stdin.readline())
rooms = []
for i in range(n):
    room =list(map(int,sys.stdin.readline().split()))

rooms.sort()
