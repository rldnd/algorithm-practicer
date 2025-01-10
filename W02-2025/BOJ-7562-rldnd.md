# [[BOJ] 나이트의 이동](https://www.acmicpc.net/problem/7562)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색]

## 발상

- 경로를 탐색하는 방법이기에 BFS를 쓰자.
- 최소 이동 횟수를 구하기 때문에, 방문했다는 표시 대신 도달하는데에 걸리는 이동 횟수를 적도록 한다.
- 특정 위치에 도달하려 할 때, 현재 위치까지 오는데 걸린 횟수 + 1과 해당 위치에 도달하는데 걸리는 이동 횟수를 비교하여 최소 값을 세팅한다.

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

test_count = int(readline())

def get_night_move_counts():
    size = int(readline())
    cur_row, cur_col = map(int, readline().split())
    des_row, des_col = map(int, readline().split())

    if cur_row == des_row and cur_col == des_col:
        return print(0)

    visit_count = [[0 for _ in range(size)] for _ in range(size)]
    queue = deque()
    queue.append((cur_row, cur_col))

    while queue:
        q_row, q_col = queue.popleft()
        for i in range(8):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny >= size or ny < 0 or nx >= size or nx < 0:
                continue
            if not visit_count[ny][nx] == 0 and visit_count[q_row][q_col] + 1 >= visit_count[ny][nx]:
                continue
            visit_count[ny][nx] = visit_count[q_row][q_col] + 1
            queue.append((ny, nx))

    print(visit_count[des_row][des_col])

for _ in range(test_count):
    get_night_move_counts()
```

- 테스트케이스에 시작점과 도착적이 같은 경우 이동 횟수는 0이길래, 확인하는 파트를 추가했음.
