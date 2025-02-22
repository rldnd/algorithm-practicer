# [[BOJ] 그림](https://www.acmicpc.net/problem/1926)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색] [깊이 우선 탐색]

## 발상

- 도화지를 순회하며, 방문하지 않았으며 그림이 존재하는 경우 큐에 삽입
- 해당 위치를 기반으로 BFS로 그림을 순회한다.

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

height, width = map(int, readline().split())
base = [list(map(int, readline().split())) for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]

count = 0
maximum = -1

for row in range(height):
    for col in range(width):
        if visited[row][col] or not base[row][col]:
            continue
        queue = deque()
        queue.append(( row, col ))
        visited[row][col] = True
        count += 1
        area = 0
        while queue:
            area += 1
            queue_row, queue_col = queue.popleft()
            for i in range(4):
                ny, nx = queue_row + dy[i], queue_col + dx[i]
                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue
                if visited[ny][nx] or not base[ny][nx]:
                    continue
                queue.append(( ny, nx ))
                visited[ny][nx] = True
        maximum = max(maximum, area)

print(count)
print(0) if maximum == -1 else print(maximum)
```

- 도화지를 순회하며, 그림이 있는 경우 해당 스코프 내에서 큐를 생성하도록 한다.
- 큐에서 시작하는 위치에서부터 순회하게 되면 하나의 그림 전체를 방문하게 되기 때문에 그림의 개수를 하나 추가한다.
- 해당 큐에 들어가는 것은 이어진 그림이 될 것이기 때문에 area에 누산.
