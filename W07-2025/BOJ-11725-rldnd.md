# [[BOJ] 트리의 부모 찾기](https://www.acmicpc.net/problem/11725)

> [그래프 이론] [그래프 탐색] [트리] [너비 우선 탐색] [깊이 우선 탐색]

## 발상

- BFS 사용

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    f, t = map(int, readline().split())
    graph[f].append(t)
    graph[t].append(f)

q = deque([1])
visited = [False] * (N + 1)
tree = {}

while q:
    a = q.popleft()
    for b in graph[a]:
        if not visited[b]:
            visited[b] = True
            q.append(b)
            tree[b] = a

for i in range(2, N + 1):
    print(tree[i])

```
