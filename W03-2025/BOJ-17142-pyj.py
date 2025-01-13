from itertools import combinations
from collections import deque

N, M = list(map(int, input().split()))

lab = []
virus = []
for x in range(N):
    info = list(map(int, input().split()))
    for y in range(N):
        if info[y] == 1:
            info[y] = "-"
        elif info[y] == 2:
            virus.append((x, y))
            info[y] = "*"
        else:
            info[y] = -1

    lab.append(info)

startVirus = combinations(virus, M)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def getTime(time, cLab):
    global N

    for x in range(N):
        for y in range(N):
            if cLab[x][y] == -1:
                return float("inf")
    return time


answer = float("inf")
for sv in startVirus:
    viruses = list(sv)

    cLab = [l[:] for l in lab]
    visited = [[False] * N for i in range(N)]

    for x, y in viruses:
        cLab[x][y] = 0
        visited[x][y] = True

    time = 0
    queue = deque(viruses)
    while queue:

        x, y = queue.popleft()

        cTime = lab[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[nx][ny]
                and cLab[nx][ny] != "-"
            ):
                if cLab[nx][ny] == -1:
                    cLab[nx][ny] = cLab[x][y] + 1
                    time = max(time, cLab[nx][ny])
                elif cLab[nx][ny] == "*":
                    cLab[nx][ny] = cLab[x][y] + 1

                visited[nx][ny] = True

                queue.append((nx, ny))

    answer = min(answer, getTime(time, cLab))

if answer == float("inf"):
    print(-1)
else:
    print(answer)
"""
3 5
2 0 2
1 2 1
2 0 2
"""
