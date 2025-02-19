# [[BOJ] 가장 긴 바이토닉 부분 수열](https://www.acmicpc.net/problem/11054)

> [다이나믹 프로그래밍]

## 발상

- DP 사용해보자

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 중간에 꺾이는 지점을 결정하는 로직이 애매한 것 같다.
- 근데 반례는 다 맞아서 짜증...

```python
import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

MAXIMUM = -1
DP = [[1, 1, False] for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        cur, comparison = A[i], A[j]
        if cur > comparison:
            DP[i][0] = max(DP[j][0] + 1, DP[i][0])
        if cur < comparison:
            if DP[j][1] + 1 > DP[i][1]:
                DP[i][2] = DP[j][2]
                DP[i][1] = DP[j][1] + 1

            if DP[i][1] < (DP[j][0] + 1) and DP[j][2] == False:
                DP[i][2] = True
                DP[i][1] = DP[j][0] + 1

    MAXIMUM = max(*DP[i], MAXIMUM)

print(MAXIMUM)
```

## <br>정답 코드

- 다른 풀이들을 보고 이해했음
- 왼쪽에서부터 오른쪽으로 증가하는 DP, 오른쪽에서 왼쪽으로 증가하는 DP 두개를 만들어서 특정 위치에서의 maximum값을 알면 된다.. 똑똑하네

```python
import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

INCREASE_DP = [1] * N
DECREASE_DP = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            INCREASE_DP[i] = max(INCREASE_DP[i], INCREASE_DP[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j]:
            DECREASE_DP[i] = max(DECREASE_DP[i], DECREASE_DP[j] + 1)

result = 0
for i in range(N):
    result = max(result, INCREASE_DP[i] + DECREASE_DP[i] - 1)

print(result)
```
