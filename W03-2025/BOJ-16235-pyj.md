# [[BOJ] {나무 제테크} - G3](https://www.acmicpc.net/problem/16235)

> [구현]

## 발상

> 따로 발상이라기 보다는 문제의 조건을 잘 따라서 구현하면 되는 문제

## <br>정답 코드

```python
N, M, K = list(map(int, input().split()))

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

trees = [[[] for i in range(N)] for i in range(N)]

for i in range(M):
    x, y, z = list(map(int, input().split()))
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

"""
가장 처음 양분 : 모든 칸 5
나무 M개 구매
한 칸에 여러개 나무 가능

봄 : 나이만큼 양분, 나이 +1, 나이가 어린 나무부터 양분, 양분이 부족 -> 나무 DIE
여름 : 죽은 나무가 양분 (죽은 나무 나이 // 2)
가을 :(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1),
(r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 에 나이 1인 나무 생성
겨울 : 양분 추가
"""

foods = [[5] * N for i in range(N)]


def springAndSummer():
    global foods, trees, N
    extraFoods = []
    for x in range(N):
        for y in range(N):
            if len(trees[x][y]) == 0:
                continue
            trees[x][y].sort()
            delIdx = -1

            for tIdx, targetTree in enumerate(trees[x][y]):

                ## 양분이 부족한 경우
                if targetTree > foods[x][y]:
                    if delIdx == -1:
                        delIdx = tIdx
                    extraFoods.append((x, y, targetTree // 2))

                ## 양분이 부족하지 않은 경우
                else:

                    foods[x][y] -= targetTree
                    trees[x][y][tIdx] += 1

            if delIdx != -1:
                trees[x][y] = trees[x][y][:delIdx]

    for x, y, food in extraFoods:
        foods[x][y] += food


def fall():
    global foods, trees, N

    for x in range(N):
        for y in range(N):

            for tree in trees[x][y]:
                if tree % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].append(1)


def winter():
    global arr, foods, N

    for x in range(N):
        for y in range(N):
            foods[x][y] += arr[x][y]


for i in range(K):
    springAndSummer()
    fall()
    winter()

answer = 0
for x in range(N):
    for y in range(N):
        answer += len(trees[x][y])

print(answer)

```
