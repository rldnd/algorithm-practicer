# [[BOJ] 특정한 최단 경로](https://www.acmicpc.net/problem/1504)

> [그래프 이론] [최단 경로] [데이크스트라]

## 발상

- v1, v2를 무조건 거쳐야 하기 때문에, 1 -> v1 -> v2 -> N, 1 -> v2 -> v1 -> N 중 최단 경로를 출력

## <br>정답 코드

```python
import sys
import heapq
readline = sys.stdin.readline

INF = float('inf')

N, E = map(int, readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

# 반드시 거쳐야 하는 두 개의 정점
v1, v2 = map(int, readline().split())

from_one_heap = [(0, 1)]
from_one_d = [INF] * (N + 1)
from_one_d[1] = 0

v1_v2_heap = [(0, v1)]
v1_v2_d = [INF] * (N + 1)
v1_v2_d[v1] = 0

v2_N_heap = [(0, v2)]
v2_N_d = [INF] * (N + 1)
v2_N_d[v2] = 0

while from_one_heap:
    w, v = heapq.heappop(from_one_heap)
    if not from_one_d[v] == w:
        continue
    for distance, destination in graph[v]:
        if w + distance < from_one_d[destination]:
            from_one_d[destination] = w + distance
            heapq.heappush(from_one_heap, (w + distance, destination))

while v1_v2_heap:
    w, v = heapq.heappop(v1_v2_heap)
    if not v1_v2_d[v] == w:
        continue
    for distance, destination in graph[v]:
        if w + distance < v1_v2_d[destination]:
            v1_v2_d[destination] = w + distance
            heapq.heappush(v1_v2_heap, (w + distance, destination))

while v2_N_heap:
    w, v = heapq.heappop(v2_N_heap)
    if not v2_N_d[v] == w:
        continue
    for distance, destination in graph[v]:
        if w + distance < v2_N_d[destination]:
            v2_N_d[destination] = w + distance
            heapq.heappush(v2_N_heap, (w + distance, destination))

v1_v2_N = from_one_d[v1] + v1_v2_d[v2] + v2_N_d[N]
v2_v1_N = from_one_d[v2] + v1_v2_d[v2] + v1_v2_d[N]

print(-1) if min(v1_v2_N, v2_v1_N) == INF else print(min(v1_v2_N, v2_v1_N))

```
