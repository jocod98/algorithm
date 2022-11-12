from collections import deque

def solution(begin, target, words):
    
    def chg(word1,word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        if cnt == 1:
            return True
        else:
            return False
    q = deque([(begin, 0)])
    visited = [begin]
    answer = [(begin,0)]
    
    while q :
        (word1,depth) = q.popleft()
        if word1 == target:
            return depth 
        for word2 in words:
            if word2 not in visited and chg(word1, word2) == True:
                q.append((word2, depth + 1))
                visited.append(word2)
    return 0
                
                

print(
    solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
