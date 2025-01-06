R, C, M = list(map(int, input().split()))

sharks = []
for i in range(M):
    sharks.append(list(map(int, input().split())))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]


def getReverseDirection(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    elif d == 4:
        return 3


def moveSharks():
    global sharks, dx, dy, R, C
    newSharks = []

    for idx, shark in enumerate(sharks):
        # (r,c) 상어위치, s 속력, d 방향, z 크기
        r, c, s, d, z = shark

        for i in range(s):
            nx = r + dx[d]
            ny = c + dy[d]

            if 1 <= nx <= R and 1 <= ny <= C:
                r = nx
                c = ny
            else:
                d = getReverseDirection(d)
                r = r + dx[d]
                c = c + dy[d]

        newSharks.append([r, c, s, d, z])
    sharks = newSharks


def eatShark():
    global sharks, M, R, C

    maps = [[[] for j in range(C + 1)] for i in range(R + 1)]
    targets = set()

    for shark in sharks:

        r, c, s, d, z = shark

        maps[r][c].append([z, r, c, s, d])

        targets.add((r, c))

    newShark = []

    for x, y in targets:

        maps[x][y].sort()

        z, r, c, s, d = maps[x][y][-1]
        newShark.append([r, c, s, d, z])

    sharks = newShark


def fish(y):
    global R, sharks
    fishShark = []
    for x in range(1, R + 1):
        targets = [shark for shark in sharks if shark[0] == x and shark[1] == y]

        if len(targets) == 0:
            continue

        fishShark.append(targets[0])
        break
    sharks = [tmpShark for tmpShark in sharks if tmpShark not in fishShark]
    return fishShark


fishSharkSum = 0
for i in range(1, C + 1):
    fShark = fish(i)

    if len(fShark) > 0:
        fishSharkSum += sum([z for r, c, s, d, z in fShark])
    moveSharks()

    eatShark()

print(fishSharkSum)
