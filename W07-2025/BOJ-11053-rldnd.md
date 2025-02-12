# [[BOJ] 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)

> [다이나믹 프로그래밍]

## 발상

- 생각해내는데 진짜 오래걸렸는데, 특정 인덱스의 값 A를 기준으로 잡고 앞에서부터 값의 크기를 비교해가며, A의 값이 해당 값보다 크다면, A에 해당하는 DP의 값에 해당 값 + 1을 대입

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

DP = [1] * N

for i in range(N):
    for j in range(i + 1):
        if A[j] < A[i]:
            DP[i] = max(DP[j] + 1, DP[i])

print(max(DP))
```
