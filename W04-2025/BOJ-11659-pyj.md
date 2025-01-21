# [[BOJ] 구간 합 구하기4](https://www.acmicpc.net/problem/11659)

> [DP]

## 발상

> 구간 합의 차를 구하는 문제

## <br>정답 코드

```python
N, M = list(map(int, input().split()))
numbs = list(map(int, input().split()))

ranges = []

for _ in range(M):
    ranges.append(list(map(int, input().split())))


sumArr = []

sumArr.append(numbs[0])
for i in range(1, N):
    sumArr.append(sumArr[i - 1] + numbs[i])
sumArr = [0, *sumArr]

for start, end in ranges:

    print(sumArr[end] - sumArr[start - 1])

```
