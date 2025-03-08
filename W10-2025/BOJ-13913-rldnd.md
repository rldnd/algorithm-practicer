# [[BOJ] 숨바꼭질 4](https://www.acmicpc.net/problem/13913)

> [그래프 이론] [그래프 탐색] [너비 우선 탐색]

## 발상

- BFS로 처리. DP로도 처리는 가능할 것 같은데, DP 테이블에 지나온 위치들을 저장하게 되면 메모리 초과가 일어날 듯하니 BFS로

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 지나온 길을 배열로 처리하면 조금 더 시간이 오래 걸리나봄..

```python
import sys
from collections import deque
readline = sys.stdin.readline

N, K = map(int, readline().split())
queue = deque([(0, N, [])])
visited = [False] * 200_001

while queue:
    times, point, pre = queue.popleft()

    if point == K:
        print(times)
        print(*[*pre, point])
        break

    for next_point in [point - 1, point + 1, point * 2]:
        if 0 <= next_point < 200_001 and not visited[next_point]:
            visited[next_point] = True
            queue.append((times + 1, next_point, [*pre, point]))

```

## <br>정답 코드

- 지나온 길 string 형태로 저장

```python
import sys
from collections import deque
readline = sys.stdin.readline

N, K = map(int, readline().split())
queue = deque([(0, N, f'{N}')])
visited = [False] * 200_001

while queue:
    times, point, pre = queue.popleft()

    if point == K:
        print(times)
        print(pre)
        break

    for next_point in [point - 1, point + 1, point * 2]:
        if 0 <= next_point < 200_001 and not visited[next_point]:
            visited[next_point] = True
            queue.append((times + 1, next_point, f'{pre} {next_point}'))

```
