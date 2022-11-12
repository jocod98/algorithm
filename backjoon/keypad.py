import numpy as np
import sys
import math

numbers = list(map(int,sys.stdin.readline().split()))
hand = sys.stdin.readline().strip()
result = []
keypad = np.array([[1,2,3],[4,5,6],[7,8,9]])
last_L = [3,0]
last_R = [3,2]
idx = []
for i in range(3):
    for j in range(3):
        idx.append(list(map(int,np.where(keypad ==keypad[i,j] ))))
for num in numbers:
    if num in [1,4,7]:
        result.append('L')
        last_L = idx[num-1]
    elif num in [3,6,9]:
        result.append('R')
        last_R = idx[num-1]
    else:
        dist1 =abs(idx[num-1][0]-last_L[0])+abs(idx[num-1][1]-last_L[1])
        dist2 =abs(idx[num-1][0]-last_R[0])+abs(idx[num-1][1]-last_R[1])
        if dist1 > dist2:
            result.append('R')
            last_R = idx[num-1]
        elif dist1<dist2:
            result.append('L')
            last_L = idx[num-1]
        else: 
            if hand == 'right': 
                result.append('R')
                last_R = idx[num-1]
            elif hand =='left':
                result.append('L')
                last_L = idx[num-1]

print(result)
