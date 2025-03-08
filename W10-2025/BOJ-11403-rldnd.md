# [[BOJ] 경로 찾기](https://www.acmicpc.net/problem/11403)

> [그래프 이론] [그래프 탐색] [최단 경로] [플로이드-워셜]

## 발상

- 흠,, 이 문제에서 원한 풀이 방식인지는 모르겠으나, BFS로 풀이.

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline())
graph = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, readline().split()))
    for j in range(N):
        if row[j]:
            graph[i].append(j)

for i in range(N):
    visited = [0] * N
    queue = deque([i])

    while queue:
        v = queue.popleft()
        for j in graph[v]:
            if not visited[j]:
                visited[j] = 1
                queue.append(j)
    print(*visited)
```
