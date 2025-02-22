# [[Programmers] [PCCP 기출문제]2번 / 석유시추](https://school.programmers.co.kr/learn/courses/30/lessons/250136)

> [BFS]

## 발상

- BFS를 사용해야 한다.
- 모든 배열을 순회하며, 석유가 존재하고 방문하지 않은 위치라면,
  - area, rows, visited, queue를 해당 스코프에서 생성한다.
  - 상하좌우로 bfs를 진행하며, 방문한 적이 없고 석유가 있다면 area 누산, rows에 열 값을 추가, visited처리, queue에 append를 반복한다.
  - bfs가 끝난 시점에 rows에 들어있는 열들에 대해서 area 값을 모두 추가해놓는다.
- 열들에 대한 area 값중 max를 리턴

## <br>정답 코드

-

```python
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def solution(land):
    height, width = len(land), len(land[0])
    visited = [[0 for _ in range(width)] for _ in range(height)]
    col_area = [0 for _ in range(width)]

    for row in range(height):
        for col in range(width):
            if not land[row][col] or visited[row][col]:
                continue
            area = 1
            rows = set()
            rows.add(col)
            visited[row][col] = 1
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for i in range(4):
                    ny, nx = dy[i] + r, dx[i] + c
                    if ny < 0 or ny >= height or nx < 0 or nx >= width or not land[ny][nx] or visited[ny][nx]:
                        continue
                    area += 1
                    rows.add(nx)
                    visited[ny][nx] = 1
                    q.append((ny, nx))

            for r in rows:
                col_area[r] += area

    return max(col_area)
```
