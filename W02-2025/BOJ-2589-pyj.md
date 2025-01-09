# [[BOJ] {보물섬} G5](<[문제링크](https://www.acmicpc.net/problem/2589)>)

> [구현] [BFS]

> BFS와 간단한 DP(배열로 값 저장하는 방법)를 사용하면 됩니다.

## 발상

> N,M이 각각 50 이하이기 때문에 전체 탐색을 할 수 있다.
> 각 2 지점의 최단거리를 bfs와 2중 배열을 통해 통해 최신화 가능

## <br>정답 코드

> search 함수에서는 BFS를 실행함과 동시에 newMaps에 시작점으로부터의 최단 거리를 저장
> 최단 거리 중에서 최장 거리를 L인 곳마다 비교를 해주면 된다.

```python
from collections import deque

N, M = list(map(int, input().split()))

maps = []


for i in range(N):
    maps.append(list(input()))

treasure = None


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def search(sx, sy):
    global dx, dy, maps, N, M

    newMaps = [[float("inf")] * M for i in range(N)]
    visited = [[False] * M for i in range(N)]
    targets = []

    queue = deque([(sx, sy, 0)])
    visited[sx][sy] = True

    while queue:
        cx, cy, count = queue.popleft()

        newMaps[cx][cy] = min(newMaps[cx][cy], count)
        targets.append((cx, cy))

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < M
                and not visited[nx][ny]
                and maps[nx][ny] == "L"
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    result = (0, 0, 0)
    for tx, ty in targets:
        rx, ry, rC = result
        if newMaps[tx][ty] > rC:
            result = (tx, ty, newMaps[tx][ty])
    rx, ry, rc = result
    return rc


answer = 0
for x in range(N):
    for y in range(M):
        if maps[x][y] == "L":
            answer = max(search(x, y), answer)

print(answer)

```
