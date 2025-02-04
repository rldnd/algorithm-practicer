# [[BOJ] 최단경로](https://www.acmicpc.net/problem/1753)

> [그래프 이론] [최단 경로] [데이크스트라]

## 발상

- 다익스트라 처음 써보니까 연습 하는 겸..

## <br>정답 코드

```python
import sys
import heapq

readline = sys.stdin.readline

INF = float('inf')

V, E = map(int, readline().split())
K = int(readline())

graph = [[] for _ in range(V + 1)]
d = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, readline().split())
    graph[u].append((v, w))

pq = [(0, K)]
d[K] = 0

while pq:
    distance, start = heapq.heappop(pq)
    if not distance == d[start]:
        continue
    for (v, w) in graph[start]:
        if distance + w < d[v]:
            d[v] = distance + w
            pq.append((distance + w, v))

for distance in d[1:]:
    print("INF") if distance == INF else print(distance)

```
