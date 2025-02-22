# [[BOJ] {ATM}](https://www.acmicpc.net/problem/11399)

> [DP]

## 발상

> 누적합의 기초

## <br>정답 코드

```python
N = int(input())
P = list(map(int, input().split()))

P.sort()

arr = [0] * N
arr[0] = P[0]

for i in range(1, N):

    arr[i] = arr[i - 1] + P[i]


print(sum(arr))

```
