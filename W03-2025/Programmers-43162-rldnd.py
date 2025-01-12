from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i]:
            continue
        answer += 1
        visited[i] = True
        q = deque()
        q.append(i)
                
        while q:
            j = q.popleft()
            for key, k in enumerate(computers[j]):
                if visited[key] or not k:
                    continue
                q.append(key)
                visited[key] = True
            
    return answer