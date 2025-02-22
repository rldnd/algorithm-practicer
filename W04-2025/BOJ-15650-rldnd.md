# [[BOJ] N과 M(2)](https://www.acmicpc.net/problem/15650)

> [백트래킹]

## 발상

- 백트래킹 포맷에서, 값을 사용할 때 증가하는 순서인지 같이 체크

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

used = [False] * (N + 1)
arr = [0] * M

def back_tracking(idx):
    global used, arr, N

    if idx == len(arr):
        return print(*arr)

    for i in range(1, N + 1):
        if not used[i] and (idx == 0 or (idx > 0 and arr[idx - 1] < i)):
            used[i] = True
            arr[idx] = i
            back_tracking(idx + 1)
            used[i] = False

back_tracking(0)
```
