# [[BOJ] 스티커](https://www.acmicpc.net/problem/9465)

> [다이나믹 프로그래밍]

## 발상

- 조건을 보니 O(NlogN)을 만족해야 하는데, 아무리봐도 DP를 사용해 column별로 잘라서 봐야할 것 같았다.
- DP테이블을 사용해 0번째 row 선택, 1번째 row 선택, 아무것도 선택하지 않는 경우를 누산해놓는 방식으로 처리하자.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

"""
n <= 100_000
최대 시간복잡도 O(nlogn)
"""

EMPTY = -1

T = int(readline())

for _ in range(T):
    n = int(readline())
    sticker = [list(map(int, readline().split())) for _ in range(2)]
    """
    0: 0번째 row / 1: 1번째 row / 2: 아무것도 선택 X
    """
    DP = [[EMPTY] * 3 for _ in range(n)]
    DP[0][0] = sticker[0][0]
    DP[0][1] = sticker[1][0]
    DP[0][2] = 0

    for col in range(1, n):
        DP[col][0] = max(DP[col - 1][1] + sticker[0][col], DP[col - 1][2] + sticker[0][col])
        DP[col][1] = max(DP[col - 1][0] + sticker[1][col], DP[col - 1][2] + sticker[1][col])
        DP[col][2] = max(*DP[col - 1])
    print(max(DP[-1]))
```
