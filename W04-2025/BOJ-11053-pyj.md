# [[BOJ] 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)

> [DP]

## 발상

> 가장 마지막 수열을 기준으로 이전 수열의 부분 수열 개수로 업데이트

## <br>정답 코드

```python
N = int(input())
A = list(map(int, input().split()))


dp = [1] * N


for i in range(1, N):

    for j in range(i):

        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))

```
