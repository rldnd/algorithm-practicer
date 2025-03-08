# [[BOJ] 구간 합 구하기 5](https://www.acmicpc.net/problem/11660)

> [다이나믹 프로그래밍] [누적 합]

## 발상

- DP 테이블을 생성해서, (1,1) 부터 해당 위치까지의 값을 누산해놓자.
- 직접 그려보면, DP 값을 이용해서 누산합을 구할 때 겹치는 부분이 생기기때문에 해당 부분을 빼면 된다.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
graph = [list(map(int, readline().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        DP[i][j] = graph[i][j]
        if i > 0 and j > 0:
            DP[i][j] += (DP[i - 1][j] + DP[i][j - 1] - DP[i - 1][j - 1])
        elif i > 0:
            DP[i][j] += DP[i - 1][j]
        elif j > 0:
            DP[i][j] += DP[i][j - 1]

for _ in range(M):
    y1, x1, y2, x2 = map(lambda x: int(x) - 1, readline().split())
    answer = DP[y2][x2]
    if x1 > 0 and y1 > 0:
       answer -= (DP[y2][x1 - 1] + DP[y1 - 1][x2] - DP[y1 - 1][x1 - 1])
    elif x1 > 0:
        answer -= DP[y2][x1 - 1]
    elif y1 > 0:
        answer -= DP[y1 - 1][x2]
    print(answer)

```
