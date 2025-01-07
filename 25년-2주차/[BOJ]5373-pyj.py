T = int(input())

result = []

cube = [[""] * 9 for i in range(12)]


def rotateClock(newCube, cube, xRange, yRange):
    xs, xe = xRange
    ys, ye = yRange

    for x in range(xs, xe + 1):
        for y in range(ys, ye + 1):
            newCube[y][xe - x] = cube[x][y]


def rotateReverseClock(newCube, cube, xRange, yRange):
    xs, xe = xRange
    ys, ye = yRange

    for x in range(xs, xe + 1):
        for y in range(ys, ye + 1):
            newCube[ye - y][x] = cube[x][y]


def updateCube(newCube, cube, lines):

    for src, dest in lines:
        srcX, srcY = src
        destX, destY = dest
        newCube[destX][destY] = cube[srcX][srcY]


"""
0 2  3 5  6 8
000  000  000 0
000  000  000
000  000  000 2
  
000  000  000 3
000  000  000
000  000  000 5

000  000  000 6
000  000  000
000  000  000 8

000  000  000 9
000  000  000
000  000  000 11
"""


# (3,3) ~ (5,5)
def spinUp(cube, direction):
    newCube = [[cube[x][y] for y in range(9)] for x in range(12)]
    lines = []
    if direction == "-":
        rotateReverseClock(newCube, cube, (3, 5), (3, 5))
        lines = [
            # 위쪽 -> 왼쪽
            ((2, 3), (5, 2)),
            ((2, 4), (4, 2)),
            ((2, 5), (3, 2)),
            # 왼쪽 -> 아래쪽
            ((3, 2), (6, 3)),
            ((4, 2), (6, 4)),
            ((5, 2), (6, 5)),
            # 아래쪽 -> 오른쪽
            ((6, 3), (5, 6)),
            ((6, 4), (4, 6)),
            ((6, 5), (3, 6)),
            # 오른쪽 -> 위쪽
            ((3, 6), (2, 3)),
            ((4, 6), (2, 4)),
            ((5, 6), (2, 5)),
        ]
    else:
        rotateClock(newCube, cube, (3, 5), (3, 5))
        lines = [
            # 위쪽 -> 오른쪽
            ((2, 3), (3, 6)),
            ((2, 4), (4, 6)),
            ((2, 5), (5, 6)),
            # 오른쪽 -> 아래쪽
            ((3, 6), (6, 5)),
            ((4, 6), (6, 4)),
            ((5, 6), (6, 3)),
            # 아래쪽 -> 왼쪽
            ((6, 5), (5, 2)),
            ((6, 4), (4, 2)),
            ((6, 3), (3, 2)),
            # 왼쪽 -> 위쪽
            ((5, 2), (2, 3)),
            ((4, 2), (2, 4)),
            ((3, 2), (2, 5)),
        ]
    updateCube(newCube, lines)
    return newCube


# (9,3) ~ (11,5)
def spinDown(cube, direction):
    newCube = [row[:] for row in cube]
    if direction == "-":
        rotateReverseClock(newCube, cube, (9, 11), (3, 5))
        lines = [
            ((8, 3), (5, 0)),
            ((8, 4), (4, 0)),
            ((8, 5), (3, 0)),  # 위 → 왼
            ((5, 0), (0, 5)),
            ((4, 0), (0, 4)),
            ((3, 0), (0, 3)),  # 왼 → 아래
            ((0, 5), (3, 8)),
            ((0, 4), (4, 8)),
            ((0, 3), (5, 8)),  # 아래 → 오른
            ((3, 8), (8, 3)),
            ((4, 8), (8, 4)),
            ((5, 8), (8, 5)),  # 오른 → 위
        ]
    else:
        rotateClock(newCube, cube, (9, 11), (3, 5))
        lines = [
            ((8, 3), (3, 8)),
            ((8, 4), (4, 8)),
            ((8, 5), (5, 8)),  # 위 → 오른
            ((3, 8), (0, 5)),
            ((4, 8), (0, 4)),
            ((5, 8), (0, 3)),  # 오른 → 아래
            ((0, 5), (5, 0)),
            ((0, 4), (4, 0)),
            ((0, 3), (3, 0)),  # 아래 → 왼
            ((5, 0), (8, 3)),
            ((4, 0), (8, 4)),
            ((3, 0), (8, 5)),  # 왼 → 위
        ]
    updateCube(newCube, lines)
    return newCube


# (6,3) ~ (8,5)
def spinFront(cube, direction):
    newCube = [row[:] for row in cube]
    if direction == "-":
        rotateReverseClock(newCube, cube, (6, 8), (3, 5))
        lines = [
            ((3, 3), (5, 0)),
            ((3, 4), (4, 0)),
            ((3, 5), (3, 0)),  # 위 → 왼
            ((5, 0), (9, 3)),
            ((4, 0), (9, 4)),
            ((3, 0), (9, 5)),  # 왼 → 아래
            ((9, 3), (5, 6)),
            ((9, 4), (4, 6)),
            ((9, 5), (3, 6)),  # 아래 → 오른
            ((5, 6), (3, 3)),
            ((4, 6), (3, 4)),
            ((3, 6), (3, 5)),  # 오른 → 위
        ]
    else:
        rotateClock(newCube, cube, (6, 8), (3, 5))
        lines = [
            ((3, 3), (5, 6)),
            ((3, 4), (4, 6)),
            ((3, 5), (3, 6)),  # 위 → 오른
            ((5, 6), (9, 5)),
            ((4, 6), (9, 4)),
            ((3, 6), (9, 3)),  # 오른 → 아래
            ((9, 5), (5, 0)),
            ((9, 4), (4, 0)),
            ((9, 3), (3, 0)),  # 아래 → 왼
            ((5, 0), (3, 3)),
            ((4, 0), (3, 4)),
            ((3, 0), (3, 5)),  # 왼 → 위
        ]
    updateCube(newCube, lines)
    return newCube


# (0,3) ~ (2,5)
def spinBack(cube, direction):
    newCube = [row[:] for row in cube]
    if direction == "-":
        rotateReverseClock(newCube, cube, (0, 2), (3, 5))
        lines = [
            ((3, 3), (5, 6)),
            ((3, 4), (4, 6)),
            ((3, 5), (3, 6)),  # 위 → 오른
            ((5, 6), (11, 5)),
            ((4, 6), (11, 4)),
            ((3, 6), (11, 3)),  # 오른 → 아래
            ((11, 5), (5, 0)),
            ((11, 4), (4, 0)),
            ((11, 3), (3, 0)),  # 아래 → 왼
            ((5, 0), (3, 3)),
            ((4, 0), (3, 4)),
            ((3, 0), (3, 5)),  # 왼 → 위
        ]
    else:
        rotateClock(newCube, cube, (0, 2), (3, 5))
        lines = [
            ((3, 3), (5, 0)),
            ((3, 4), (4, 0)),
            ((3, 5), (3, 0)),  # 위 → 왼
            ((5, 0), (11, 3)),
            ((4, 0), (11, 4)),
            ((3, 0), (11, 5)),  # 왼 → 아래
            ((11, 3), (5, 6)),
            ((11, 4), (4, 6)),
            ((11, 5), (3, 6)),  # 아래 → 오른
            ((5, 6), (3, 3)),
            ((4, 6), (3, 4)),
            ((3, 6), (3, 5)),  # 오른 → 위
        ]
    updateCube(newCube, lines)
    return newCube


# (3,0) ~ (5,2)
def spinLeft(cube, direction):
    newCube = [row[:] for row in cube]
    if direction == "-":
        rotateReverseClock(newCube, cube, (3, 5), (0, 2))
        lines = [
            ((3, 0), (5, 2)),
            ((4, 0), (4, 2)),
            ((5, 0), (3, 2)),  # 위 → 왼
            ((5, 2), (9, 0)),
            ((4, 2), (9, 1)),
            ((3, 2), (9, 2)),  # 왼 → 아래
            ((9, 0), (5, 6)),
            ((9, 1), (4, 6)),
            ((9, 2), (3, 6)),  # 아래 → 오른
            ((5, 6), (3, 0)),
            ((4, 6), (4, 0)),
            ((3, 6), (5, 0)),  # 오른 → 위
        ]
    else:
        rotateClock(newCube, cube, (3, 5), (0, 2))
        lines = [
            ((3, 0), (5, 6)),
            ((4, 0), (4, 6)),
            ((5, 0), (3, 6)),  # 위 → 오른
            ((5, 6), (9, 2)),
            ((4, 6), (9, 1)),
            ((3, 6), (9, 0)),  # 오른 → 아래
            ((9, 2), (5, 2)),
            ((9, 1), (4, 2)),
            ((9, 0), (3, 2)),  # 아래 → 왼
            ((5, 2), (3, 0)),
            ((4, 2), (4, 0)),
            ((3, 2), (5, 0)),  # 왼 → 위
        ]
    updateCube(newCube, lines)
    return newCube


# (3,6) ~ (5,8)
def spinRight(cube, direction):
    newCube = [row[:] for row in cube]
    if direction == "-":
        rotateReverseClock(newCube, cube, (3, 5), (6, 8))
        lines = [
            ((3, 6), (5, 8)),
            ((4, 6), (4, 8)),
            ((5, 6), (3, 8)),  # 위 → 왼
            ((5, 8), (9, 6)),
            ((4, 8), (9, 7)),
            ((3, 8), (9, 8)),  # 왼 → 아래
            ((9, 6), (5, 0)),
            ((9, 7), (4, 0)),
            ((9, 8), (3, 0)),  # 아래 → 오른
            ((5, 0), (3, 6)),
            ((4, 0), (4, 6)),
            ((3, 0), (5, 6)),  # 오른 → 위
        ]
    else:
        rotateClock(newCube, cube, (3, 5), (6, 8))
        lines = [
            ((3, 6), (5, 0)),
            ((4, 6), (4, 0)),
            ((5, 6), (3, 0)),  # 위 → 오른
            ((5, 0), (9, 8)),
            ((4, 0), (9, 7)),
            ((3, 0), (9, 6)),  # 오른 → 아래
            ((9, 8), (5, 8)),
            ((9, 7), (4, 8)),
            ((9, 6), (3, 8)),  # 아래 → 왼
            ((5, 8), (3, 6)),
            ((4, 8), (4, 6)),
            ((3, 8), (5, 6)),  # 왼 → 위
        ]
    updateCube(newCube, lines)
    return newCube


def initCube():
    cube = [[""] * 9 for i in range(12)]
    # 위
    for x in range(3, 6):
        for y in range(3, 6):
            cube[x][y] = "w"
    # 아래
    for x in range(9, 12):
        for y in range(3, 6):
            cube[x][y] = "y"
    # 앞
    for x in range(6, 9):
        for y in range(3, 6):
            cube[x][y] = "r"
    # 뒤
    for x in range(0, 3):
        for y in range(3, 6):
            cube[x][y] = "o"
    # 왼
    for x in range(3, 6):
        for y in range(0, 3):
            cube[x][y] = "g"

    # 오
    for x in range(3, 6):
        for y in range(6, 9):
            cube[x][y] = "b"

    return cube


def spinCube(cube, spin):
    side, direction = spin.split()

    if side == "U":
        return spinUp(cube, direction)
    elif side == "D":
        return spinDown(cube, direction)
    elif side == "F":
        return spinFront(cube, direction)
    elif side == "B":
        return spinBack(cube, direction)
    elif side == "L":
        return spinLeft(cube, direction)
    elif side == "R":
        return spinRight(cube, direction)


for i in range(T):
    N = int(input())
    spins = input().split()
    cube = initCube()

    # for spin in spins:
    #     cube = spinCube(cube, spin)

    result.append(cube[3][3] + cube[3][4] + cube[3][5])


for r in result:
    print(r)
