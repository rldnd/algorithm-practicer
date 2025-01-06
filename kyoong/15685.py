N = int(input())
dragons = []

for i in range(N):
    dragons.append(list(map(int, input().split())))


"""
x축 : 오른쪽
y축 : 아래쪽
드래곤 커브 (시작점, 시작방향, 세대)

0세대 : (0,0) - (1,0)


0 ->  1
1 -> 2
2 -> 3
3 - >1

"""

maps = [[0] * 101 for _ in range(101)]

directionDict = {0: 1, 1: 2, 2: 3, 3: 0}
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for dragon in dragons:
    x, y, d, g = dragon
    maps[x][y] = 1
    direction = [d]

    for _ in range(g):
        for i in range(len(direction) - 1, -1, -1):
            direction.append(directionDict[direction[i]])

    for direct in direction:
        x, y = x + dx[direct], y + dy[direct]

        maps[x][y] = 1


square = 0
for x in range(100):
    for y in range(100):
        if (
            maps[x][y] == 1
            and maps[x + 1][y] == 1
            and maps[x][y + 1] == 1
            and maps[x + 1][y + 1] == 1
        ):
            square += 1


print(square)
