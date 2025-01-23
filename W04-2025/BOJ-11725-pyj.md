# [[BOJ] 트리의 부모 찾기](https://www.acmicpc.net/problem/11725)

> [BFS]

## 발상

> 간단한 bfs 문제

## <br>정답 코드

```python
from collections import deque

N = int(input())

nodes = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    nodes[a].append(b)
    nodes[b].append(a)

tree = dict()


queue = deque([1])


while queue:
    parent = queue.popleft()

    for child in nodes[parent]:

        if not tree.get(child):

            tree[child] = parent
            queue.append(child)


for i in range(2, N + 1):
    print(tree[i])

```
