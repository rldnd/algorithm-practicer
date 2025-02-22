# [[BOJ] 1로 만들기](https://www.acmicpc.net/problem/1463)

> [BFS] [DP]

## <br> BFS 정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

X = int(readline())
visited = [0 for _ in range(X + 1)]
queue = deque()
queue.append((X, 0))
visited[X] = 1

while queue:
    x, trys = queue.popleft()
    if x == 1:
        print(trys)
        break

    for i in range(3):
        value = 0
        if i == 0 and x % 3 == 0 and not visited[x // 3]:
            queue.append((x // 3, trys + 1))
            visited[x // 3] = 1
        if i == 1 and x % 2 == 0 and not visited[x // 2]:
            queue.append((x // 2, trys + 1))
            visited[x // 2] = 1
        if i == 2 and x > 1 and not visited[x - 1]:
            queue.append((x - 1, trys + 1))
            visited[x - 1] = 1
```

## <br> DP정답 코드

- 규칙 찾기 너무 어려워..

```python
import sys
readline = sys.stdin.readline

X = int(readline())

DP = [0 for _ in range(X + 1)]

for i in range(2, X + 1):
    DP[i] = DP[i - 1] + 1
    if not i % 3:
        DP[i] = min(DP[i // 3] + 1, DP[i])
    if not i % 2:
        DP[i] = min(DP[i // 2] + 1, DP[i])

print(DP[X])
```
