# [[2606] {바이러스}](https://www.acmicpc.net/problem/2606)

> [그래프] [BFS]

## 발상

> 방문한 노드의 수를 구하면 된다

## <br>정답 코드

```python
from collections import deque

N = int(input())
M = int(input())
computers = [[] for i in range(N + 1)]

for i in range(M):
    a, b = list(map(int, input().split()))
    computers[a].append(b)
    computers[b].append(a)


visited = [False] * (N + 1)
queue = deque([1])
visited[1] = True

while queue:
    current = queue.popleft()

    for comp in computers[current]:
        if not visited[comp]:
            visited[comp] = True
            queue.append(comp)

print(visited.count(True) - 1)

```
