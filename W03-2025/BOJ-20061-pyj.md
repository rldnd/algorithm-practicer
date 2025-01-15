# [[BOJ] {모노미노도미노2} - G2](<(https://www.acmicpc.net/problem/20061)>)

> [구현]

## 발상

> 차근차근 문제에서 주어진 조건에 따라서 구현을 해야한다.

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 블록을 지울 때 0번째 인덱스에 블록이 채워져 있는 경우를 생각을 안함

```python
N = int(input())


blue = [[0] * 6 for i in range(4)]
green = [[0] * 4 for i in range(6)]
score = 0


#     # t, x, y
#     # t = 1  1x1 블록 (x,y)
#     # t = 2  1x2 블록 (x,y) (x, y + 1)
#     # t = 3  2x1 블록 (x,y) (x + 1, y)


## 가득찬 행 또는 열 -> 점수 먼저 획득 후 연한 칸 제거


def deleteBlueBlock():
    global blue

    for y in range(0, 2):
        isExists = any(blue[x][y] == 1 for x in range(4))

        if not isExists:
            continue

        for x in range(4):
            blue[x][5] = 0

        for ty in range(4, -1, -1):
            for x in range(4):
                blue[x][ty + 1] = blue[x][ty]


def deleteGreenBlock():
    global green
    for x in range(0, 2):
        isExists = any(green[x][y] == 1 for y in range(4))

        if not isExists:
            continue

        for y in range(4):
            green[5][y] = 0

        for tx in range(4, -1, -1):
            for y in range(4):
                green[tx + 1][y] = green[tx][y]


def scoreBlueBlock():
    global blue, score
    targetY = []
    for y in range(6):
        isClear = all(blue[x][y] == 1 for x in range(4))
        if isClear:
            targetY.append(y)
            score += 1

    for ty in targetY:
        for x in range(4):
            blue[x][ty] = 0
            for ny in range(ty, -1, -1):
                if ny == 0:
                    blue[x][ny] = 0
                else:
                    blue[x][ny] = blue[x][ny - 1]


def scoreGreenBlock():
    global green, score
    targetX = []
    for x in range(6):
        isClear = all(green[x][y] == 1 for y in range(4))

        if isClear:
            targetX.append(x)
            score += 1
    for tx in targetX:
        for y in range(4):
            green[tx][y] = 0
            for nx in range(tx, -1, -1):
                if nx == 0:
                    green[nx][y] == 0
                else:
                    green[nx][y] = green[nx - 1][y]


def moveBlueBlock(block):
    global blue

    t, x, y = block
    if t == 1:
        block = [(x, 0)]
    elif t == 2:
        block = [(x, 0), (x, 1)]

    elif t == 3:
        block = [(x, 0), (x + 1, 1)]

    if t == 1:
        startYIdx = 0

        while True:
            x, y = block[0]
            if startYIdx + 1 == 6 or blue[x][startYIdx + 1] == 1:
                blue[x][startYIdx] = 1
                break

            startYIdx += 1

    elif t == 2:

        endYIdx = 1

        while True:
            sx, sy = block[0]
            nx, ny = block[1]

            if endYIdx + 1 == 6 or blue[nx][endYIdx + 1] == 1:
                blue[nx][endYIdx] = 1
                blue[nx][endYIdx - 1] = 1
                break

            endYIdx += 1

    elif t == 3:

        endYIdx = 0
        while True:
            sx, sy = block[0]
            nx, ny = block[1]

            if (
                endYIdx + 1 == 6
                or blue[nx][endYIdx + 1] == 1
                or blue[sx][endYIdx + 1] == 1
            ):
                blue[sx][endYIdx] = 1
                blue[nx][endYIdx] = 1
                break

            endYIdx += 1

    scoreBlueBlock()
    deleteBlueBlock()


def moveGreenBlock(block):
    global green

    t, x, y = block
    if t == 1:
        block = [(0, y)]
    elif t == 2:
        block = [(0, y), (0, y + 1)]

    elif t == 3:
        block = [(0, y), (1, y)]

    if t == 1:
        startXIdx = 0

        while True:
            x, y = block[0]
            if startXIdx + 1 == 6 or green[startXIdx + 1][y] == 1:
                green[startXIdx][y] = 1
                break

            startXIdx += 1

    elif t == 2:

        endXIdx = 1

        while True:
            sx, sy = block[0]
            nx, ny = block[1]

            if (
                endXIdx + 1 == 6
                or green[endXIdx + 1][sy] == 1
                or green[endXIdx + 1][ny] == 1
            ):
                green[endXIdx][sy] = 1
                green[endXIdx][ny] = 1
                break

            endXIdx += 1

    elif t == 3:

        endXIdx = 1
        while True:

            nx, ny = block[1]

            if endXIdx + 1 == 6 or green[endXIdx + 1][ny] == 1:
                green[endXIdx - 1][ny] = 1
                green[endXIdx][ny] = 1
                break

            endXIdx += 1

    scoreGreenBlock()
    deleteGreenBlock()


def locateBlock(block):
    global blue, green

    moveBlueBlock(block)
    moveGreenBlock(block)


for i in range(N):
    block = list(map(int, input().split()))

    locateBlock(block)


count = 0

for b in blue:
    count += b.count(1)

for g in green:
    count += g.count(1)

print(score)
print(count)

```

## <br>정답 코드

> _정답 코드 및 구현한 내용 중 설명한 부분이 있다면, 내용을 적어주세요._

```python
N = int(input())


blue = [[0] * 6 for i in range(4)]
green = [[0] * 4 for i in range(6)]
score = 0


#     # t, x, y
#     # t = 1  1x1 블록 (x,y)
#     # t = 2  1x2 블록 (x,y) (x, y + 1)
#     # t = 3  2x1 블록 (x,y) (x + 1, y)


## 가득찬 행 또는 열 -> 점수 먼저 획득 후 연한 칸 제거


def deleteBlueBlock():
    global blue
    existsCount = 0
    for y in range(0, 2):
        isExists = any(blue[x][y] == 1 for x in range(4))

        if not isExists:
            continue

        existsCount += 1
    for i in range(existsCount):
        for x in range(4):
            blue[x][5] = 0

        for ty in range(4, -1, -1):
            for x in range(4):
                blue[x][ty + 1] = blue[x][ty]

        for x in range(4):
            blue[x][0] = 0


def deleteGreenBlock():
    global green
    exitsCount = 0
    for x in range(0, 2):
        isExists = any(green[x][y] == 1 for y in range(4))

        if not isExists:
            continue
        exitsCount += 1
    for i in range(exitsCount):

        for y in range(4):
            green[5][y] = 0

        for tx in range(4, -1, -1):
            for y in range(4):
                green[tx + 1][y] = green[tx][y]

        for y in range(4):
            green[0][y] = 0


def scoreBlueBlock():
    global blue, score
    targetY = []
    for y in range(6):
        isClear = all(blue[x][y] == 1 for x in range(4))
        if isClear:
            targetY.append(y)
            score += 1

    for ty in targetY:
        for x in range(4):
            blue[x][ty] = 0
            for ny in range(ty, -1, -1):
                if ny == 0:
                    blue[x][ny] = 0
                else:
                    blue[x][ny] = blue[x][ny - 1]


def scoreGreenBlock():
    global green, score
    targetX = []
    for x in range(6):
        isClear = all(green[x][y] == 1 for y in range(4))

        if isClear:
            targetX.append(x)
            score += 1
    for tx in targetX:
        for y in range(4):
            green[tx][y] = 0
            for nx in range(tx, -1, -1):
                if nx == 0:
                    green[nx][y] == 0
                else:
                    green[nx][y] = green[nx - 1][y]


def moveBlueBlock(block):
    global blue

    t, x, y = block
    if t == 1:
        block = [(x, 0)]
    elif t == 2:
        block = [(x, 0), (x, 1)]

    elif t == 3:
        block = [(x, 0), (x + 1, 1)]

    if t == 1:
        startYIdx = 0

        while True:
            x, y = block[0]
            if startYIdx + 1 == 6 or blue[x][startYIdx + 1] == 1:
                blue[x][startYIdx] = 1
                break

            startYIdx += 1

    elif t == 2:

        endYIdx = 1

        while True:
            sx, sy = block[0]
            nx, ny = block[1]

            if endYIdx + 1 == 6 or blue[nx][endYIdx + 1] == 1:
                blue[nx][endYIdx] = 1
                blue[nx][endYIdx - 1] = 1
                break

            endYIdx += 1

    elif t == 3:

        endYIdx = 0
        while True:
            sx, sy = block[0]
            nx, ny = block[1]

            if (
                endYIdx + 1 == 6
                or blue[nx][endYIdx + 1] == 1
                or blue[sx][endYIdx + 1] == 1
            ):
                blue[sx][endYIdx] = 1
                blue[nx][endYIdx] = 1
                break

            endYIdx += 1

    scoreBlueBlock()
    deleteBlueBlock()


def moveGreenBlock(block):
    global green

    t, x, y = block
    if t == 1:
        block = [(0, y)]
    elif t == 2:
        block = [(0, y), (0, y + 1)]

    elif t == 3:
        block = [(0, y), (1, y)]

    if t == 1:
        startXIdx = 0

        while True:
            x, y = block[0]
            if startXIdx + 1 == 6 or green[startXIdx + 1][y] == 1:
                green[startXIdx][y] = 1
                break

            startXIdx += 1

    elif t == 2:

        endXIdx = 1

        while True:
            sx, sy = block[0]
            nx, ny = block[1]

            if (
                endXIdx + 1 == 6
                or green[endXIdx + 1][sy] == 1
                or green[endXIdx + 1][ny] == 1
            ):
                green[endXIdx][sy] = 1
                green[endXIdx][ny] = 1
                break

            endXIdx += 1

    elif t == 3:

        endXIdx = 1
        while True:

            nx, ny = block[1]

            if endXIdx + 1 == 6 or green[endXIdx + 1][ny] == 1:
                green[endXIdx - 1][ny] = 1
                green[endXIdx][ny] = 1
                break

            endXIdx += 1

    scoreGreenBlock()
    deleteGreenBlock()


def locateBlock(block):
    global blue, green

    moveBlueBlock(block)
    moveGreenBlock(block)


for i in range(N):
    block = list(map(int, input().split()))

    locateBlock(block)


count = 0

for b, g in zip(blue, green):
    count += b.count(1)
    count += g.count(1)


print(score)
print(count)

```
