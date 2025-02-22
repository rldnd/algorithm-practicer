# [[Programmers] 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

> [BFS]

## 발상

> computers는 정점에서의 연결된 다른 정점들을 알 수 있는 지표이다.
> 모든 컴퓨터를 순회하며 방문하지 않았다면 visit 처리, 네트워크 개수 + 1을 한 이후, 그 점에서부터 연결된 모든 컴퓨터들을 방문처리한다.

## <br>정답 코드

```python
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
```
