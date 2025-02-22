# [[BOJ] 불](https://www.acmicpc.net/problem/5427)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색]

## 발상

- 경로를 탐색하는 방법이기에 BFS를 쓰자.
- 불의 탐색을 우선적으로 진행한 뒤, 사람이 탐색하도록 진행하자.

## <br> 틀린 풀이 코드 및 틀린 이유

```python
import sys
from collections import deque
readline = sys.stdin.readline

test_case_count = int(readline())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_escape_road_count():
    width, height = map(int, readline().split())
    # False는 접근 불가, True는 접근 가능
    building = []
    fires = []
    fire_visit = [[0] * width for _ in range(height)]
    fire_queue = deque()
    start = []
    per_visit = [[0] * width for _ in range(height)]
    per_queue = deque()
    minimum = 1e9

    for i in range(height):
        line = list(readline().rstrip())
        row = []
        for key, char in enumerate(line):
            if char == '#':
                row.append(False)
            else:
                row.append(True)
                if char == '@':
                    start.append((i, key))
                    per_queue.append((i, key))
                    per_visit[i][key] = 1
                if char == '*':
                    fires.append((i, key))
                    fire_queue.append((i, key))
                    fire_visit[i][key] = 1
        building.append(row)

    while fire_queue:
        q_row, q_col = fire_queue.popleft()
        for i in range(4):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                continue
            if building[ny][nx] and not fire_visit[ny][nx]:
                fire_visit[ny][nx] = fire_visit[q_row][q_col] + 1
                fire_queue.append((ny, nx))


    while per_queue:
        q_row, q_col = per_queue.popleft()
        for i in range(4):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                minimum = min(minimum, per_visit[q_row][q_col])
                continue
            if building[ny][nx] and (not fire_visit[ny][nx] or per_visit[q_row][q_col] < fire_visit[ny][nx]):
                per_visit[ny][nx] = per_visit[q_row][q_col] + 1
                per_queue.append((ny, nx))

    print(minimum) if minimum != 1e9 else print('IMPOSSIBLE')

for _ in range(test_case_count):
    get_escape_road_count()
```

- 메모리 초과가 떴다. 배열을 두개 써서 그런가 싶다. _~~배열 문제 아니었음~~_
- bfs의 경우, 어차피 최단 시간의 접근을 생각하기 때문에, minimum을 굳이 사용할 필요는 없다.

1. 사람이 순회할 때 사람이 visit했는지에 대해 체크를 하지 않기 때문에, 사람이 벽에 둘러쌓여있다면 무한루프
2. `불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다` 라는 조건이 있기 때문에 per_visit[q_row][q_col] < fire_visit[ny][nx] 조건은 잘못됨.

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

test_case_count = int(readline())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_escape_road_count():
    width, height = map(int, readline().split())
    # False는 접근 불가, True는 접근 가능
    building = []
    fire_visit = [[0] * width for _ in range(height)]
    fire_queue = deque()
    per_visit = [[0] * width for _ in range(height)]
    per_queue = deque()

    for i in range(height):
        line = list(readline().rstrip())
        row = []
        for key, char in enumerate(line):
            if char == '#':
                row.append(False)
            else:
                row.append(True)
                if char == '@':
                    per_queue.append((i, key))
                    per_visit[i][key] = 1
                if char == '*':
                    fire_queue.append((i, key))
                    fire_visit[i][key] = 1
        building.append(row)

    while fire_queue:
        q_row, q_col = fire_queue.popleft()
        for i in range(4):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                continue
            if building[ny][nx] and (not fire_visit[ny][nx] or fire_visit[q_row][q_col] + 1 < fire_visit[ny][nx]):
                fire_visit[ny][nx] = fire_visit[q_row][q_col] + 1
                fire_queue.append((ny, nx))


    while per_queue:
        q_row, q_col = per_queue.popleft()
        for i in range(4):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                return print(per_visit[q_row][q_col])
            if building[ny][nx] and not per_visit[ny][nx] and (not fire_visit[ny][nx] or per_visit[q_row][q_col] + 1 < fire_visit[ny][nx]):
                per_visit[ny][nx] = per_visit[q_row][q_col] + 1
                per_queue.append((ny, nx))

    print('IMPOSSIBLE')

for _ in range(test_case_count):
    get_escape_road_count()
```
