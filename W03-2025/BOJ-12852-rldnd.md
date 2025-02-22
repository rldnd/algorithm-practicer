# [[BOJ] 1로 만들기 2](문제링크)

> [DP]

## 발상

- i번째 수의 연산 횟수를 구할때에는 i - 1, i / 3, i / 2 중 제일 작은 횟수 + 1을 하게 될 것.
- 그에 대해 방법에 포함된 수의 경우, 저장 공간을 따로 만들기로 함.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N = int(readline())

DP = [0] * (N + 1)
history = [[] for _ in range(N+1)]

DP[1] = 0
history[1] = [1]

test = [1,2,3,4]

for i in range(2, N + 1):
    DP[i] = DP[i - 1] + 1
    history[i] = [*history[i - 1], i]

    if not i % 3 and DP[i // 3] + 1 < DP[i]:
        DP[i] = DP[i // 3] + 1
        history[i] = [*history[i // 3], i]
    if not i % 2 and DP[i // 2] + 1 < DP[i]:
        DP[i] = DP[i // 2] + 1
        history[i] = [*history[i // 2], i]

print(DP[N])
for i in reversed(history[N]):
    print(i, end = ' ')
```
