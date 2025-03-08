# [[BOJ] 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색]

## 발상

- BFS를 쓰되 큐에 벽을 부순 적이 있는지 정보를 포함해야 함.
- visited 배열을 3중 배열로 해서 부수고 접근했는지, 안부수고 접근했는지를 같이 저장

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

WALL = 1

ny = [-1, 0, 1, 0]
nx = [0, -1, 0, 1]

N, M = map(int, readline().split())
"""
N x M
"""
graph = [list(map(int, list(readline().rstrip()))) for _ in range(N)]
# (breaked_visited, not_breaked_visited)
breaked_visited = [[[False, False] for _ in range(M)] for _ in range(N)]

# row, col, count, breaked
q = deque()
q.append((0, 0, 1, False))
breaked_visited[0][0][1] = True

answer = -1

while q:
    row, col, count, breaked = q.popleft()
    if row == N - 1 and col == M - 1:
        answer = count
        break

    for i in range(4):
        dy = row + ny[i]
        dx = col + nx[i]
        if 0 <= dy < N and 0 <= dx < M:
            if graph[dy][dx] == WALL and not breaked and not breaked_visited[dy][dx][breaked]:
                breaked_visited[dy][dx][breaked] = True
                q.append((dy, dx, count + 1, True))
            if not graph[dy][dx] == WALL and not breaked_visited[dy][dx][breaked]:
                breaked_visited[dy][dx][breaked] = True
                q.append((dy, dx, count + 1, breaked))

print(answer)
```
