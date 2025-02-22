# [[BOJ] Z](https://www.acmicpc.net/problem/1074)

> [재귀] [DP]

## 발상

> 사각형을 4등분을 계속 하는 방식으로 재귀함수를 돌려야함

## <br>정답 코드

> 모든 칸을 검색하면 시간초과가 날 수 밖에 없다
> 찾고 싶은 칸이 4등분 중 어느 영역에 있는지 알면 된다.

```python
N, x, y = list(map(int, input().split()))

count = 0
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def recursive(deps, start, startValue):
    global x, y, dx, dy

    sx, sy = start

    if deps == 1:
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if nx == x and ny == y:
                print(startValue + i)
                return

    # N = 3, (0,0) -> (0,0) (0,4) (4,0) (4,4)
    # N = 2, (0,4)  -> (0,4) (0,6) (6,4) (6,6)
    lux, luy = start
    rux, ruy = (sx, sy + 2 ** (deps - 1))
    ldx, ldy = (sx + 2 ** (deps - 1), sy)
    rdx, rdy = (sx + 2 ** (deps - 1), sy + 2 ** (deps - 1))
    plusValue = (2**deps) * (2**deps) // 4 if deps > 2 else 4

    # 왼쪽 위
    if lux <= x < ldx and luy <= y < ruy:
        recursive(deps - 1, start, startValue)
    # 오른쪽 위
    if lux <= x < ldx and ruy <= y:
        recursive(deps - 1, (rux, ruy), startValue + plusValue)

    # 왼쪽 아래
    if ldx <= x and luy <= y < ruy:

        recursive(deps - 1, (ldx, ldy), startValue + plusValue * 2)

    # 오른쪽 아래
    if rdx <= x and rdy <= y:
        recursive(deps - 1, (rdx, rdy), startValue + plusValue * 3)


recursive(N, (0, 0), 0)

```
