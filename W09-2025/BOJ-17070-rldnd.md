# [[BOJ] ](문제링크)

> [BFS] [백트래킹]

> _위와 같이 만약 사용한 알고리즘 기술 및 자료구조가 있다면, 적어주세요._

## 발상

> _풀이를 떠오르게된 과정을 상세히 적어주시면 됩니다._

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 시간초과

```python
import sys
readline = sys.stdin.readline

EMPTY, WALL = 0, 1

N = int(readline())
graph = [list(map(int, readline().split())) for _ in range(N)]

answer = 0

RIGHT = 'right'
DOWN = 'down'
RIGHT_DOWN = 'right_down'

RIGHT_ENABLED_Y_X_DIRECTION = [(0, 1, RIGHT), (1, 1, RIGHT_DOWN)]
DOWN_ENABLED_Y_X_DIRECTION = [(1, 0, DOWN), (1, 1, RIGHT_DOWN)]
RIGHT_DOWN_ENABLED_Y_X_DIRECTION = [(0, 1, RIGHT), (1, 1, RIGHT_DOWN), (1, 0, DOWN)]

def dfs(r, c, direction):
    global answer

    if r == N - 1 and c == N - 1:
        answer += 1
        return

    if direction == RIGHT:
        for y, x, d in RIGHT_ENABLED_Y_X_DIRECTION:
            row = r + y
            col = c + x
            if row < 0 or col < 0 or row >= N or col >= N or graph[row][col] == WALL or (d == RIGHT_DOWN and (graph[row - 1][col] == WALL or graph[row][col - 1] == WALL)):
                continue
            dfs(row, col, d)
    if direction == DOWN:
        for y, x, d in DOWN_ENABLED_Y_X_DIRECTION:
            row = r + y
            col = c + x
            if row < 0 or col < 0 or row >= N or col >= N or graph[row][col] == WALL or (d == RIGHT_DOWN and (graph[row - 1][col] == WALL or graph[row][col - 1] == WALL)):
                continue
            dfs(row, col, d)
    if direction == RIGHT_DOWN:
        for y, x, d in RIGHT_DOWN_ENABLED_Y_X_DIRECTION:
            row = r + y
            col = c + x
            if row < 0 or col < 0 or row >= N or col >= N or graph[row][col] == WALL or (d == RIGHT_DOWN and (graph[row - 1][col] == WALL or graph[row][col - 1] == WALL)):
                continue
            dfs(row, col, d)

dfs(0, 1, RIGHT)
print(answer)
```

## <br>정답 코드

- 캐시를 사용한 방법.
- dfs로 처리하다가 보면, 같은 위치를 다른 방식으로 접근할 수 있는 일이 생긴다.
- 그때 어차피 똑같은 위치와 방향으로 접근했다면, 그 순간부터의 연산은 모두 똑같기때문에 cache를 사용

```python
import sys
readline = sys.stdin.readline

EMPTY, WALL = 0, 1

N = int(readline())
graph = [list(map(int, readline().split())) for _ in range(N)]

RIGHT = 'right'
DOWN = 'down'
RIGHT_DOWN = 'right_down'

RIGHT_ENABLED_Y_X_DIRECTION = [(0, 1, RIGHT), (1, 1, RIGHT_DOWN)]
DOWN_ENABLED_Y_X_DIRECTION = [(1, 0, DOWN), (1, 1, RIGHT_DOWN)]
RIGHT_DOWN_ENABLED_Y_X_DIRECTION = [(0, 1, RIGHT), (1, 1, RIGHT_DOWN), (1, 0, DOWN)]

cache = {}

def dfs(r, c, direction):
    if (r, c, direction) in cache:
        return cache[(r, c, direction)]

    if r == N - 1 and c == N - 1:
        return 1

    count = 0
    if direction == RIGHT:
        enabled = RIGHT_ENABLED_Y_X_DIRECTION
    elif direction == DOWN:
        enabled = DOWN_ENABLED_Y_X_DIRECTION
    else:
        enabled = RIGHT_DOWN_ENABLED_Y_X_DIRECTION

    for y, x, d in enabled:
        row = r + y
        col = c + x
        if row < 0 or col < 0 or row >= N or col >= N or graph[row][col] == WALL or (d == RIGHT_DOWN and (graph[row - 1][col] == WALL or graph[row][col - 1] == WALL)):
            continue
        count += dfs(row, col, d)

    cache[(r, c, direction)] = count
    return count

print(dfs(0, 1, RIGHT))
```
