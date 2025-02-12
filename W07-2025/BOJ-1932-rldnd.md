# [[BOJ] 정수 삼각형](https://www.acmicpc.net/problem/1932)

> [다이나믹 프로그래밍]

## 발상

- 왜인지 모르겠지만, 이런 문제보면 바로 백트래킹 써버리고 싶은데, 시간초과날 것 같아서 다시 생각해보니 DP를 사용하기로 했다.
- 특정 삼각형 위치에 해당 위치에서 가질 수 있는 최대의 값을 가지도록 DP 테이블 생성.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

n = int(readline())

triangle = [list(map(int, readline().split())) for _ in range(n)]
DP = [[0] * i for i in range(1, n + 1)]
DP[0][0] = triangle[0][0]

for row in range(1, n):
    for col in range(row + 1):
        if col:
            DP[row][col] = max(DP[row][col], DP[row - 1][col - 1] + triangle[row][col])
        if not col == row:
            DP[row][col] = max(DP[row][col], DP[row - 1][col] + triangle[row][col])
print(max(DP[-1]))

```
