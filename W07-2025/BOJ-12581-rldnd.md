# [[BOJ] 숨바꼭질](https://www.acmicpc.net/problem/12851)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색]

## 발상

## <br>정답 코드

- 특정 위치를 방문할 때, 걸린 시간을 visited 배열에 저장하고, 해당 index의 visited 값이 방문하는데에 걸린 시간보다 크거나 같다면 방문처리

```python
import sys
from collections import deque
readline = sys.stdin.readline

INF = float('inf')

N, K = map(int, readline().split())
queue = deque([(0, N)])
visited = [INF] * 100_001
visited[N] = 0

answer = 0
times = 0

while queue:
    time, point = queue.popleft()
    if point == K:
        answer = time
        times += 1
        continue
    for next in [point + 1, point - 1, point * 2]:
        if next < 0 or next > 100_000:
            continue
        if visited[next] < time + 1:
            continue
        visited[next] = time + 1
        queue.append((time + 1, next))

print(answer)
print(times)
```
