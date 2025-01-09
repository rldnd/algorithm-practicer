N = int(input())

teams = []
for i in range(N):
    teams.append(list(map(int, input().split())))


# 방문한게 스타트 아닌게 링크
players = [False for i in range(N)]
answer = float("inf")


def dfs(start, trueCount):
    global players, N, teams, answer

    if trueCount == N // 2:
        startTeam = 0
        linkTeam = 0

        for playerOne in range(N):
            for playerTwo in range(N):
                # 스타트팀
                if players[playerOne] and players[playerTwo]:
                    startTeam += teams[playerOne][playerTwo]
                # 링크팀
                elif not players[playerOne] and not players[playerTwo]:
                    linkTeam += teams[playerOne][playerTwo]
        answer = min(answer, abs(startTeam - linkTeam))
        return

    for i in range(start, N):

        if not players[i]:
            players[i] = True
            dfs(i + 1, trueCount + 1)
            players[i] = False


dfs(0, 0)
print(answer)
