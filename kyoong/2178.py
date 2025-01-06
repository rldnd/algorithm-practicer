from collections import deque

N, M = list(map(int, input().split()))

miro = []
for i in range(N):
    miro.append(list(map(int, list(input()))))


queue = deque([(0, 0, 1)])
visited = [[False for i in range(M)] for i in range(N)]
visited[0][0] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    cx, cy, count = queue.popleft()

    if cx == N - 1 and cy == M - 1:
        print(count)
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and miro[nx][ny] != 0:
            visited[nx][ny] = True
            queue.append((nx, ny, count + 1))
