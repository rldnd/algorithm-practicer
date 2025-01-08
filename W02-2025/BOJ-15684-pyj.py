from itertools import combinations

N, M, H = list(map(int, input().split()))

lines = []
for i in range(M):
    a, b = list(map(int, input().split()))
    # a : 가로선, b b + 1 : 세로선
    lines.append([a, b, b + 1])


candis = []


for h in range(1, H + 1):
    for n in range(1, N):
        candi = [h, n, n + 1]

        isOk = True
        for a, b, bp in lines:
            # 겹치는 경우
            if h == a and b == n and bp == n + 1:
                isOk = False

            # 연속하는 경우 오른쪽으로
            if h == a and n + 1 == b:
                isOk = False
            # 연속하는 경우 왼쪽으로
            if h == a and n == bp:
                isOk = False
        if isOk:
            candis.append(candi)

answer = -1


def sadari(tLines):

    ladder = {h: {} for h in range(1, H + 1)}
    for h, b1, b2 in tLines:
        ladder[h][b1] = b2
        ladder[h][b2] = b1

    for start in range(1, N + 1):
        current = start
        for h in range(1, H + 1):
            if current in ladder[h]:
                current = ladder[h][current]
        if current != start:
            return False

    return True


def start():
    global candis, answer
    for p in range(4):
        crosses = list(combinations(candis, p))  # N ^ 2

        for cross in crosses:  #
            testLines = [*lines, *cross]

            result = sadari(testLines)  # H

            if result:

                answer = p
                return


start()
print(answer)
