N, M, x, y, K = list(map(int, input().split()))

maps = []

for i in range(N):
    maps.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

dice = [[0] * 3 for i in range(4)]

"""

  2
4 1 3
  5
  6


"""


def rollDice(direction):
    global dice

    ## 동쪽
    if direction == 1:
        left, up, right, down = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
        dice[1][0] = down
        dice[1][1] = left
        dice[1][2] = up
        dice[3][1] = right

    ## 서쪽
    elif direction == 2:
        left, up, right, down = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
        dice[1][0] = up
        dice[1][1] = right
        dice[1][2] = down
        dice[3][1] = left

    ## 북쪽
    elif direction == 3:
        one, two, three, four = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
        dice[0][1] = two
        dice[1][1] = three
        dice[2][1] = four
        dice[3][1] = one

    ## 남쪽
    elif direction == 4:

        one, two, three, four = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
        dice[0][1] = four
        dice[1][1] = one
        dice[2][1] = two
        dice[3][1] = three


def getDiceDown():
    global dice
    return dice[3][1]


def getDiceUp():
    global dice
    return dice[1][1]


def getNextLocation(direction):
    global x, y, N, M
    ## 동쪽 이동
    if direction == 1:
        if y + 1 >= M:
            return None
        return (x, y + 1)
    ## 서쪽 이동
    elif direction == 2:
        if y - 1 < 0:
            return None
        return (x, y - 1)

    ## 북쪽 이동
    elif direction == 3:
        if x - 1 < 0:
            return None
        return (x - 1, y)
    ## 남쪽 이동
    elif direction == 4:
        if x + 1 >= N:
            return None
        return (x + 1, y)


for direction in directions:
    nextLocation = getNextLocation(direction)

    if not nextLocation:
        continue
    nx, ny = nextLocation
    rollDice(direction)

    diceDown = getDiceDown()

    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[3][1]
    else:
        dice[3][1] = maps[nx][ny]
        maps[nx][ny] = 0

    x, y = nx, ny
    print(getDiceUp())
