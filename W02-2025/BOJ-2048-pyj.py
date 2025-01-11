N = 5

# boards = []

# for i in range(N):
#     boards.append(list(map(int, input().split())))


def count(cBoard):
    global N
    score = 0
    for x in range(N):
        for y in range(N):
            score += cBoard[x][y]

    return score


def sumStack(stack):
    # global N
    N = len(stack)
    sIdx = 0
    while sIdx < N:
        print(sIdx, stack)
        if stack[sIdx] == 0 and stack[sIdx + 1] == 0:
            startIdx = sIdx + 1
            while startIdx < N:
                print(startIdx, stack[startIdx])

                if stack[startIdx] != 0:
                    print("여기")
                    stack[sIdx] = stack[startIdx]
                    stack[startIdx] = 0
                    break
                else:
                    startIdx += 1
            print(startIdx)
            sIdx = startIdx

        elif stack[sIdx] == stack[sIdx + 1]:
            print("둘이 같아")
            stack[sIdx] *= 2
            stack[sIdx + 1] = 0

        elif stack[sIdx] == 0 and stack[sIdx + 1] != 0:
            print("한칸 땡겨")
            stack[sIdx] = stack[sIdx + 1]
            stack[sIdx + 1] = 0

        sIdx += 1

    print(stack)


sumStack([2, 0, 0, 0, 8])


def up(cBoard):
    global N

    nBoard = [[0] * N for _ in range(N)]

    for y in range(N):

        stack = []
        for x in range(N):
            stack.append(cBoard[x][y])

        # 2 2 4 8
        # 4 0 4 8
        # 4 4 0 8
        # 4 4 8 0
        # 8 0 8 0
        # 8 8 0 0
        # 16 0 0 0


def left(cBoard):
    global N
    nBoard = [[0] * N for _ in range(N)]


def right(cBoard):
    global N
    nBoard = [[0] * N for _ in range(N)]


def down(cBoard):
    global N
    nBoard = [[0] * N for _ in range(N)]


directions = ["UP", "LEFT", "RIGHT", "DOWN"]


maxScore = 0


def dfs(direction, count, cBoard):
    global maxScore, directions
    if count == 5:
        maxScore = max(count(cBoard), maxScore)
        return
    if direction == "UP":
        nBoard = up(cBoard)
        for d in directions:
            dfs(d, count + 1, nBoard)
    elif direction == "LEFT":
        nBoard = left(cBoard)
        for d in directions:
            dfs(d, count + 1, nBoard)
    elif direction == "RIGHT":
        nBoard = right(cBoard)
        for d in directions:
            dfs(d, count + 1, nBoard)
    else:
        nBoard = down(cBoard)
        for d in directions:
            dfs(d, count + 1, nBoard)
