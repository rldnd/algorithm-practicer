# [[BOJ] 내려가기](https://www.acmicpc.net/problem/2096)

> [다이나믹 프로그래밍] [슬라이딩 윈도우]

## 발상

- 이거 간단한 DP문제구나

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 문제의 메모리 제한이 4MB이다. DP 배열을 최대 100_000 \* 3씩 int크기로 만든다면 메모리 초과가 뜨게 된다.

```python
import sys
readline = sys.stdin.readline

N = int(readline())
graph = [list(map(int, readline().split())) for _ in range(N)]

"""
시간복잡도 O(NlogN)
"""

MAX = [[0] * 3 for _ in range(N)]
MIN = [[0] * 3 for _ in range(N)]

for i in range(3):
    MAX[0][i] = graph[0][i]
    MIN[0][i] = graph[0][i]

for i in range(1, N):
    MAX[i][0] = max(MAX[i - 1][0] + graph[i][0], MAX[i - 1][1] + graph[i][0])
    MAX[i][1] = max(MAX[i - 1][0] + graph[i][1], MAX[i - 1][1] + graph[i][1], MAX[i - 1][2] + graph[i][1])
    MAX[i][2] = max(MAX[i - 1][2] + graph[i][2], MAX[i - 1][1] + graph[i][2])

    MIN[i][0] = min(MIN[i - 1][0] + graph[i][0], MIN[i - 1][1] + graph[i][0])
    MIN[i][1] = min(MIN[i - 1][0] + graph[i][1], MIN[i - 1][1] + graph[i][1], MIN[i - 1][2] + graph[i][1])
    MIN[i][2] = min(MIN[i - 1][2] + graph[i][2], MIN[i - 1][1] + graph[i][2])

print(f'{max(MAX[-1])} {min(MIN[-1])}')
```

## <br>정답 코드

- while문을 통해 DP 테이블을 쓰지 않도록 하자.

```python
import sys
readline = sys.stdin.readline

N = int(readline())

MAX = list(map(int, readline().split()))
MIN = MAX[:]

tries = 1

while not tries == N:
    temp_max = MAX[:]
    temp_min = MIN[:]

    row = list(map(int, readline().split()))

    MAX[0] = max(temp_max[0] + row[0], temp_max[1] + row[0])
    MAX[1] = max(temp_max[0] + row[1], temp_max[1] + row[1], temp_max[2] + row[1])
    MAX[2] = max(temp_max[2] + row[2], temp_max[1] + row[2])
    MIN[0] = min(temp_min[0] + row[0], temp_min[1] + row[0])
    MIN[1] = min(temp_min[0] + row[1], temp_min[1] + row[1], temp_min[2] + row[1])
    MIN[2] = min(temp_min[2] + row[2], temp_min[1] + row[2])
    tries += 1

print(f'{max(MAX)} {min(MIN)}')
```
