# [[BOJ] N과 M(1)](https://www.acmicpc.net/problem/15649)

> [백트래킹]

## 발상

- 백트래킹 사용이 처음이라, 일단 코드의 생김새에 집중해서 최대한 틀에 익숙하게 하자.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
arr = [0 for _ in range(M)]
used = [0 for _ in range(N + 1)]

def back_tracking(idx):
    global arr, used

    if idx == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if not used[i]:
            arr[idx] = i
            used[i] = 1
            back_tracking(idx + 1)
            used[i] = 0

back_tracking(0)
```
