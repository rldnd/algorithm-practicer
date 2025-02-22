# [[BOJ] 1,2,3 더하기](<(<https://www.acmicpc.net/problem/9095)>>>)

> [DP]

## 발상

> 3으로 시작하는 경우의 수, 2로 시작하는 경우의 수, 1로 시작하는 경우의 수를 DP로 저장하면 된다.

## <br>정답 코드

```python
T = int(input())
nums = []
dp = [0] * 12
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 12):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(T):
    num = int(input())
    print(dp[num])

```
