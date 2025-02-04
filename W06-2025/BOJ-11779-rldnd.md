# [[BOJ] 최소비용 구하기2](https://www.acmicpc.net/problem/11779)

> [그래프 이론] [최단 경로] [데이크스트라]

## 발상

- 다익스트라 + 경로 복원

## <br>정답 코드

```python
import heapq
import sys

INF = float("INF")

readline = sys.stdin.readline

n = int(readline()) # 정점 개수
m = int(readline()) # 간선 개수

graph = [[] for _ in range(n + 1)]
d = [INF] * (n + 1)
pre = [0] * (n + 1)

for _ in range(m):
    s, e, w = map(int, readline().split())
    graph[s].append((e, w))

start, end = map(int, readline().split())
d[start] = 0
pq = [(0, start)]

while pq:
    distance, s = heapq.heappop(pq)
    if not d[s] == distance:
        continue
    for e, w in graph[s]:
        if distance + w < d[e]:
            pq.append((distance + w, e))
            d[e] = distance + w
            pre[e] = s

n_count = 0
n_arr = []

point = end

while point:
    n_arr.append(point)
    point = pre[point]
    n_count += 1


print(d[end])
print(n_count)
print(*reversed(n_arr))
```
