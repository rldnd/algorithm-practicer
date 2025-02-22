# [[BOJ] 숨바꼭질3](https://www.acmicpc.net/problem/12851)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색] [최단 경로] [데이크스트라] [0-1 너비 우선 탐색]

## 발상

- 단순 BFS

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

N, K = map(int, readline().split())

INF = float('inf')
queue = deque()
queue.append((0, N))
visited = [INF] * (200_001)
visited[N] = True

while queue:
    time, point = queue.popleft()
    if point == K:
        print(time)
        break
    for next_t, next_p in [(time, 2 * point), (time + 1, point - 1), (time + 1, point + 1)]:
        if next_p > 200_000 or next_p < 0:
            continue
        if visited[next_p] < next_t:
            continue
        visited[next_p] = next_t
        queue.append((next_t, next_p))
```
