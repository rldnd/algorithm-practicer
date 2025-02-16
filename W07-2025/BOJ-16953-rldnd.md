# [[BOJ] A → B](https://www.acmicpc.net/problem/16953)

> [그래프 이론] [그리디 알고리즘] [그래프 탐색] [너비 우선 탐색]

## 발상

- 그냥 BFS를 쓰면 되겠다. 근데 1을 수의 오른쪽에 추가하며 작은수에서부터 시작하는 것은 필요없이 경우의수를 만드는 경우가 될 수 있음
- 반대로 큰 수에서 작은수를 만들자

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

A, B = map(int, readline().split())

q = deque()
q.append((1, B))

while q:
    tries, value = q.popleft()
    if value == A:
        print(tries)
        break
    nx = []
    if not value % 2:
        nx.append(value // 2)
    if str(value).endswith('1'):
        next_val = str(value)[:-1]
        if next_val and int(next_val) >= A:
            nx.append(int(next_val))
    if not nx:
        print(-1)
        break
    for i in nx:
        q.append((tries + 1, i))

```
