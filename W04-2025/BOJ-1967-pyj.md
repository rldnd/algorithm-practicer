# [[BOJ] 트리의 지름](https://www.acmicpc.net/problem/1967)

> [BFS] [그래프]

## 발상

> 웰노운 문제 어쩌구 저쩌구

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 각 노드에서 가지별 거리를 잰 다음 폈을 때 최대인 길이를 추산했음
> pypy3에서는 통과이나 python에서 시간초과라 다시 풀이

```python
from collections import deque

N = int(input())

nodes = [[] for i in range(N + 1)]

for i in range(N - 1):
    parent, child, weight = list(map(int, input().split()))

    nodes[parent].append([child, weight])
    nodes[child].append([parent, weight])

answer = 0

for parentNode in range(1, N + 1):
    if len(nodes[parentNode]) <= 1:
        continue

    allDistances = []
    for childNode in nodes[parentNode]:
        visited = [False] * (N + 1)
        visited[parentNode] = True
        visited[childNode[0]] = True
        queue = deque([(childNode[0], childNode[1])])
        distances = []

        while queue:
            cNode, cDis = queue.popleft()

            isMore = False

            for nNode in nodes[cNode]:
                if not visited[nNode[0]]:
                    visited[nNode[0]] = True
                    isMore = True
                    queue.append((nNode[0], cDis + nNode[1]))

            if not isMore:

                distances.append(cDis)

        allDistances.append(max(distances))

    allDistances.sort()
    answer = max(answer, allDistances[-1] + allDistances[-2])


print(answer)
```

## <br>정답 코드

> 힌트를 좀 얻긴했다...
> 트리의 지름은 항상 점 A에서 가장 먼 지점 B로부터 가장 먼 C지점까지의 거리 즉, B-C 사이 거리다

```python
from collections import deque

N = int(input())

nodes = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    parent, child, weight = map(int, input().split())
    nodes[parent].append((child, weight))
    nodes[child].append((parent, weight))


def bfs(start):
    distances = [-1] * (N + 1)
    queue = deque([start])
    distances[start] = 0

    endNode = start
    maxDistance = 0

    while queue:
        current = queue.popleft()
        for neighbor, weight in nodes[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + weight
                queue.append(neighbor)

                if distances[neighbor] > maxDistance:
                    maxDistance = distances[neighbor]
                    endNode = neighbor

    return (endNode, maxDistance)


endNode, _ = bfs(1)


_, distance = bfs(endNode)

print(distance)

```
