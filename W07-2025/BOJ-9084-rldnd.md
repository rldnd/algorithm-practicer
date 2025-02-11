# [[BOJ] 동전](https://www.acmicpc.net/problem/9084)

> [다이나믹 프로그래밍] [배낭 문제]

## 발상

- [이 문제](https://www.acmicpc.net/problem/12865)랑 똑같은 배낭문젠데 접근 방법이 너무 다르다..
- [참고 게시물](https://d-cron.tistory.com/23)

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

T = int(readline())

for _ in range(T):
    N = int(readline())
    coins = list(map(int, readline().split()))
    price = int(readline())
    DP = [[0] * (price + 1) for _ in range(N)]

    for idx in range(N):
        DP[idx][0] = 1

    for idx in range(N):
        coin = coins[idx]
        for i in range(1, price + 1):
            if idx > 0:
                DP[idx][i] += DP[idx - 1][i]
            if i >= coin:
                DP[idx][i] += DP[idx][i - coin]
    print(DP[-1][-1])
```
