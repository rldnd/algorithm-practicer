# [[BOJ] 유기농 배추](https://www.acmicpc.net/problem/1012)

> [BFS]

## 발상

> BFS 기초

## <br>정답 코드

```python
from collections import deque

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = list(map(int, input().split()))

    fields = [[0] * M for i in range(N)]
    targets = []
    for i in range(K):
        y, x = list(map(int, input().split()))
        fields[x][y] = 1
        targets.append((x, y))

    visited = [[False] * M for i in range(N)]
    count = 0
    for x in range(N):
        for y in range(M):
            if not visited[x][y] and fields[x][y] == 1:
                queue = deque([(x, y)])
                count += 1
                visited[x][y] = True

                while queue:
                    cx, cy = queue.popleft()

                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]

                        if (
                            0 <= nx < N
                            and 0 <= ny < M
                            and not visited[nx][ny]
                            and fields[nx][ny] == 1
                        ):
                            visited[nx][ny] = True
                            queue.append((nx, ny))

    print(count)

```
