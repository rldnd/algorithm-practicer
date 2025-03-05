# [[BOJ] 파티](https://www.acmicpc.net/problem/1238)

> [그래프 이론] [최단 경로] [데이크스트파]

## 발상

- 시간 복잡도를 생각해봤을 때 조금 애매했다. O(NMlogN) 정도가 나오는데, 이게 간당간당하게 될 것 같아서, 일단 구현 해봤다.
- 시간을 따져보니, X 마을을 제외하고, A마을은 A -> X + X -> A / B마을은 B -> X + X -> B 방식으로 소요시간이 걸린다.
- 즉 X 마을을 제외하고는 해당 마을에서 X까지의 최단시간, X 마을은 각 마을까지의 최단 시간을 저장해놓고, 비교해보면 된다.

## <br>정답 코드

```python
import sys
import heapq
readline = sys.stdin.readline

N, M, X = map(int, readline().split())
INF = float('inf')
graph = [[] for _ in range(N + 1)]

d = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v, e, w = map(int, readline().split())
    graph[v].append((w, e))

for i in range(1, N + 1):
    min_heap = [(0, i)]
    d[i][i] = 0

    while min_heap:
        w, v = heapq.heappop(min_heap)
        if not d[i][v] == w:
            continue
        for weight, end in graph[v]:
            if w + weight < d[i][end]:
                d[i][end] = w + weight
                heapq.heappush(min_heap, (w + weight, end))

answer = -1
for i in range(1, N + 1):
    if i == X:
        continue
    answer = max(answer, d[X][i] + d[i][X])

print(answer)
```
