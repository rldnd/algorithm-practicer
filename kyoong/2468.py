from collections import deque

N = int(input())

regions = []
maxHeight = 0

for i in range(N):
    region = list(map(int, input().split()))
    maxHeight = max(maxHeight, *region)
    regions.append(region)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(sx, sy, visited, height):
    global regions, dx, dy, N

    visited[sx][sy] = True

    queue = deque([(sx, sy)])

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[nx][ny]
                and regions[nx][ny] > height
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))


maxCount = 0

for i in range(maxHeight + 1):
    visited = [[False] * N for i in range(N)]
    count = 0
    for x in range(N):
        for y in range(N):
            if regions[x][y] > i and not visited[x][y]:
                bfs(x, y, visited, i)
                count += 1
    maxCount = max(count, maxCount)

print(maxCount)
