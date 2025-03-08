# [[BOJ] 쉬운 최단거리](https://www.acmicpc.net/problem/14940)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색]

## 발상

- 단순 BFS이나, 0, -1이 출력되어야 하는 부분을 잘 세팅해놔야겠다.

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

BLOCKED, ROAD, GOAL = 0, 1, 2
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]

N, M = map(int, readline().split())
graph = [list(map(int, readline().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

goal_row, goal_col = -1, -1

for i in range(N):
    for j in range(M):
        if graph[i][j] == BLOCKED:
            visited[i][j] = BLOCKED
        if graph[i][j] == GOAL:
            goal_row, goal_col = i, j

queue = deque([(goal_row, goal_col, 0)])
visited[goal_row][goal_col] = 0

while queue:
    row, col, times = queue.popleft()
    for i in range(4):
        dy = row + ny[i]
        dx = col + nx[i]
        if 0 <= dy < N and 0 <= dx < M:
            if graph[dy][dx] == BLOCKED:
                visited[dy][dx] = BLOCKED
            if graph[dy][dx] == ROAD and visited[dy][dx] == -1:
                visited[dy][dx] = times + 1
                queue.append((dy, dx, times + 1))

for i in range(N):
    print(*visited[i])
```
