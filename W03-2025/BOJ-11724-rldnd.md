# [[BOJ] 연결 요소의 개수](https://www.acmicpc.net/problem/11724)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색] [깊이 우선 탐색]

## 발상

- 방향이 없는 요소기 때문에, graph 배열을 2중 배열로 만들어 graph[from][to] = True, graph[to][from] = True 모두 처리
- 여타 BFS와 같이 방문하지 않았다면 visited 처리 및 area += 1. 그리고 해당 위치에서 BFS 처리하며 visited 처리.

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

N, M = map(int, readline().split())

visited = [False for _ in range(N + 1)]
graph = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    f, t = map(int, readline().split())
    graph[f][t] = True
    graph[t][f] = True

area = 0

for i in range(1, N+1):
    if visited[i]:
        continue
    area += 1
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        a = q.popleft()
        for b in range(N + 1):
            if visited[b] or not graph[a][b]:
                continue
            q.append(b)
            visited[b] = True

print(area)
```
