# [[BOJ] 최소비용 구하기](https://www.acmicpc.net/problem/1916)

> [그래프 이론] [최단 경로] [데이크스트라]

## 발상

- 다익스트라

## <br>정답 코드

```python
import heapq
import sys

readline = sys.stdin.readline

N = int(readline())
M = int(readline())
INF = float('inf')

graph = [[] for _ in range(N + 1)]
d = [INF] * (N + 1)

for _ in range(M):
    s, v, w = map(int, readline().split())
    graph[s].append((w,v))

start, end = map(int, readline().split())
pq = [(0, start)]
d[start] = 0

while pq:
    distance, s = heapq.heappop(pq)
    if not distance == d[s]:
        continue
    for w, v in graph[s]:
        if distance + w < d[v]:
            d[v] = distance + w
            pq.append((distance + w, v))

print(d[end])
```
