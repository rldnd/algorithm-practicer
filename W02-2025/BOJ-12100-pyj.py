import copy

N = int(input())

boards = [list(map(int, input().split())) for _ in range(N)]

directions = ["UP", "LEFT", "RIGHT", "DOWN"]
maxScore = 0


def getScore(cBoard):
    return max(max(row) for row in cBoard)


def sumStack(stack):
    N = len(stack)
    nStack = [num for num in stack if num != 0] + [0] * stack.count(0)

    for i in range(N - 1):
        if nStack[i] == nStack[i + 1] and nStack[i] != 0:
            nStack[i] *= 2
            nStack[i + 1] = 0

    return [num for num in nStack if num != 0] + [0] * nStack.count(0)


def up(cBoard):
    nBoard = [[0] * N for _ in range(N)]
    for y in range(N):
        stack = [cBoard[x][y] for x in range(N)]
        stack = sumStack(stack)
        for x in range(N):
            nBoard[x][y] = stack[x]
    return nBoard


def down(cBoard):
    nBoard = [[0] * N for _ in range(N)]
    for y in range(N):
        stack = [cBoard[x][y] for x in range(N - 1, -1, -1)]
        stack = sumStack(stack)
        for x in range(N - 1, -1, -1):
            nBoard[x][y] = stack[N - 1 - x]
    return nBoard


def left(cBoard):
    nBoard = [[0] * N for _ in range(N)]
    for x in range(N):
        stack = [cBoard[x][y] for y in range(N)]
        stack = sumStack(stack)
        for y in range(N):
            nBoard[x][y] = stack[y]
    return nBoard


def right(cBoard):
    nBoard = [[0] * N for _ in range(N)]
    for x in range(N):
        stack = [cBoard[x][y] for y in range(N - 1, -1, -1)]
        stack = sumStack(stack)
        for y in range(N - 1, -1, -1):
            nBoard[x][y] = stack[N - 1 - y]
    return nBoard


def dfs(count, cBoard):
    global maxScore, directions

    if count == 5:
        maxScore = max(maxScore, getScore(cBoard))
        return

    for direction in directions:
        if direction == "UP":
            nBoard = up(copy.deepcopy(cBoard))
        elif direction == "DOWN":
            nBoard = down(copy.deepcopy(cBoard))
        elif direction == "LEFT":
            nBoard = left(copy.deepcopy(cBoard))
        else:
            nBoard = right(copy.deepcopy(cBoard))

        dfs(count + 1, nBoard)


dfs(0, boards)
print(maxScore)
