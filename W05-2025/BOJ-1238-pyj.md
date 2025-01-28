# [[BOJ] 파티](https://www.acmicpc.net/problem/1238)

> [다익스트라]

## 발상

> 각 노드에서 다른 노드로 가는 최소 경로 중 최대 경로를 구하면 되는 문제

## <br>정답 코드

```python
import heapq

N, M, X = list(map(int, input().split()))


nodes = [[] for _ in range(N + 1)]


for _ in range(M):
    start, end, t = list(map(int, input().split()))
    nodes[start].append([end, t])


def dijkstra(start):
    global nodes, N
    queue = []
    distances = [float("inf")] * (N + 1)
    distances[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        cDis, cNode = heapq.heappop(queue)

        if distances[cNode] < cDis:
            continue

        for n, nDis in nodes[cNode]:
            if cDis + nDis < distances[n]:
                distances[n] = cDis + nDis
                heapq.heappush(queue, (cDis + nDis, n))

    return distances


xDistances = dijkstra(X)


answer = 0
for i in range(1, N + 1):
    if i == X:
        continue

    iDistances = dijkstra(i)

    answer = max(iDistances[X] + xDistances[i], answer)


print(answer)

```
