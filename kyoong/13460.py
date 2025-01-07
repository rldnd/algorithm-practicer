N, M = list(map(int, input().split()))
boards = []

red, blue, goal = None, None, None
for x in range(N):
    board = list(input())
    for y in range(M):
        if board[y] == "B":
            blue = [x, y]
        if board[y] == "R":
            red = [x, y]
        if board[y] == "O":
            goal = [x, y]

    boards.append(board)
# 0 아래, 1 위, 2 오른쪽, 3 왼쪽

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def tilt(red, blue, direction):
    global boards, goal, N, M
    newRed, newBlue = red[:], blue[:]
    gx, gy = goal

    while True:
        rx, ry = newRed
        bx, by = newBlue
        rnx, rny = rx + dx[direction], ry + dy[direction]
        bnx, bny = bx + dx[direction], by + dy[direction]

        # 탈출 조건
        if boards[rnx][rny] == "#" and boards[bnx][bny] == "#":
            break

        ## 각 돌이 벽에 부딫히는지 확인

        if boards[rnx][rny] == "#":
            rnx = rx
            rny = ry

        if boards[bnx][bny] == "#":
            bnx = bx
            bny = by

        ## 돌이 겹치는지 확인
        if rnx == bnx and rny == bny:
            ## 빨간색이 움직인 경우
            if boards[bx + dx[direction]][by + dy[direction]] == "#":
                rnx = rx
                rny = ry

            ## 파란색이 움직인 경우
            if boards[rx + dx[direction]][ry + dy[direction]] == "#":
                bnx = bx
                bny = by
            newRed = rnx, rny
            newBlue = bnx, bny

            return newRed, newBlue

        # 파란 공이 들어간 경우
        if bnx == gx and bny == gy:

            return False

        # 골인한 경우
        if rnx == gx and rny == gy:
            if 0 <= bnx < N and 0 <= bny < M and not (boards[bnx][bny] == "#"):
                isFail = False
                while boards[bnx][bny] != "#":
                    bnx, bny = bnx + dx[direction], bny + dy[direction]

                    if bnx == gx and bny == gy:
                        isFail = True

                if isFail:

                    return False
                else:
                    return True

            else:

                return True

        ## 실제로 움직임
        newRed = rnx, rny
        newBlue = bnx, bny

    return newRed, newBlue


answer = float("inf")


def recursive(red, blue, count):
    global goal, answer
    gx, gy = goal
    rx, ry = red
    bx, by = blue

    if count > 10 or count > answer:
        return
    for i in range(4):

        result = tilt(red, blue, i)

        if result is False:
            continue

        elif result is True:

            answer = min(answer, count)
            continue

        else:
            newRed, newBlue = result
            nrx, nry = newRed
            nbx, nby = newBlue

            if not (
                (nrx == rx and nry == ry and nbx == bx and nby == by)
                or (boards[nrx][nry] == "#" and boards[nbx][nby] == "#")
                or (nbx == gx and nby == gy)
            ):

                recursive(newRed, newBlue, count + 1)


recursive(red, blue, 1)


if answer == float("inf"):
    print(-1)
else:
    print(answer)

"""
. : 빈칸
# : 벽
0 : 구멍
R : 빨간 구슬
B : 파란 구슬

6 8
########
#.O....#
##.#...#
#..##.R#
##B..###
########

"""
