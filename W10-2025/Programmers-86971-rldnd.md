# [[Programmers] 전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)

## 발상

- BFS 처리

## <br>정답 코드

```python
from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    answer = float('inf')

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        times = 1

        while queue:
            a = queue.popleft()
            for b in graph[a]:
                if not visited[b] and not ([v1, v2] == [a, b] or [v1, v2] == [b, a]):
                    visited[b] = True
                    queue.append(b)
                    times += 1
        answer = min(answer, abs((n - times) - times))

    return answer
```
