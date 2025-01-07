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
    ## 반시계
    if direction == "-":
        # 면 회전
        rotateReverseClock(newCube, cube, (3, 5), (3, 5))
        ## 위쪽 -> 왼쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

        ## 오른쪽 -> 위쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

        ## 왼쪽 -> 아래쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

        ## 아래쪽 -> 위쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

    ## 시계
    else:
        # 면 회전
        rotateClock(newCube, cube, (3, 5), (3, 5))
        ## 위쪽 -> 오른쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

        ## 오른쪽 -> 아래쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

        ## 왼쪽 -> 위쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

        ## 아래쪽 -> 왼쪽
        newCube[5][2], newCube[4][2], newCube[3][2] = cube[2][3], cube[2][4], cube[2][5]

    return newCube


# (9,3) ~ (11,5)
def spinDown(cube, direction):
    newCube = [[cube[x][y] for y in range(9)] for x in range(12)]
    ## 반시계
    if direction == "-":
        # 면 회전
        rotateReverseClock(newCube, cube, (9, 11), (3, 5))

    ## 시계
    else:
        # 면 회전
        rotateClock(newCube, cube, (9, 11), (3, 5))

    return newCube


# (6,3) ~ (8,5)
def spinFront(cube, direction):
    newCube = [[cube[x][y] for y in range(9)] for x in range(12)]
    ## 반시계
    if direction == "-":
        # 면 회전
        rotateReverseClock(newCube, cube, (6, 8), (3, 5))

    ## 시계
    else:
        # 면 회전
        rotateClock(newCube, cube, (6, 8), (3, 5))

    return newCube


# (0,3) ~ (2,5)
def spinBack(cube, direction):
    newCube = [[cube[x][y] for y in range(9)] for x in range(12)]
    ## 반시계
    if direction == "-":
        # 면 회전
        rotateReverseClock(newCube, cube, (0, 2), (3, 5))

    ## 시계
    else:
        # 면 회전
        rotateClock(newCube, cube, (0, 2), (3, 5))

    return newCube


# (3,0) ~ (5,2)
def spinLeft(cube, direction):

    newCube = [[cube[x][y] for y in range(9)] for x in range(12)]
    ## 반시계
    if direction == "-":
        # 면 회전
        rotateReverseClock(newCube, cube, (3, 5), (0, 2))

    ## 시계
    else:
        # 면 회전
        rotateClock(newCube, cube, (3, 5), (0, 2))

    return newCube


# (3,6) ~ (5,8)
def spinRight(cube, direction):

    newCube = [[cube[x][y] for y in range(9)] for x in range(12)]
    ## 반시계
    if direction == "-":
        # 면 회전
        rotateReverseClock(newCube, cube, (3, 5), (6, 8))

    ## 시계
    else:
        # 면 회전
        rotateClock(newCube, cube, (3, 5), (6, 8))

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
