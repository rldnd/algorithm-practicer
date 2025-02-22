# [[BOJ] N과 M(4)](https://www.acmicpc.net/problem/15652)

> [백트래킹]

## 발상

- 백트래킹 쓰기

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

arr = list(range(1, N + 1))
answer = [0] * M

def back_tracking(idx):
    if idx == M:
        return print(*answer)
    for i in arr:
        if idx == 0 or (idx > 0 and answer[idx - 1] <= i):
            answer[idx] = i
            back_tracking(idx + 1)

back_tracking(0)
```
