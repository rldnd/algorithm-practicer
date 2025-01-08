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
