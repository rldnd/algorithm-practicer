# [[BOJ] 평범한 배낭](https://www.acmicpc.net/problem/12865)

> [다이나믹 프로그래밍] [배낭 문제]

## 발상

- 흠.. 일단 다 담아보면서 최대 값을 처리해보는 방식으로 백트래킹을 써보자

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 시간초과!

```python
import sys
import heapq
readline = sys.stdin.readline

N, K = map(int, readline().split())

# W (weight), V (value)
items = [tuple(map(int, readline().split())) for _ in range(N)]
used = [False] * N
answer = 0
value = 0
weight = 0

def back_tracking():
    global answer, value, weight

    for i in range(N):
        if not used[i]:
            w, v = items[i]
            if w + weight > K:
                continue
            value += v
            weight += w
            used[i] = True
            answer = max(answer, value)
            back_tracking()
            value -= v
            weight -= w
            used[i] = False


back_tracking()
print(answer)

```

## <br>정답 코드

- 찾아보니, 배낭 문제라고 하는 이미 유명한 DP 방식이 존재하는 듯 했다.
- [해당 블로그](https://howudong.tistory.com/106) 참고

```python
import sys
readline = sys.stdin.readline

# N: 물품 수, K: 버틸 수 있는 무게
N, K = map(int, readline().split())
# W (weight), V (value) -> (w, v)
items = [tuple(map(int, readline().split())) for _ in range(N)]

"""
배낭 문제
최대이익[i][w]: 최대무게가 w인 가방에서 i번째 물건까지 판단했을 때의 최대가치
"""

DP = [[0] * (K + 1) for _ in range(N + 1)]

"""
물건의 무게가 배낭 무게를 초과할 때
DP[i + 1][w] = DP[i][w]
"""

"""
담을 수 있을 때
DP[K + 1][W] = K value + DP[K][W-M]
"""

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= items[i - 1][0]:
            DP[i][j] = max(items[i - 1][1] + DP[i - 1][j - items[i - 1][0]], DP[i - 1][j])
        else:
            DP[i][j] = DP[i - 1][j]

print(DP[N][K])
```
