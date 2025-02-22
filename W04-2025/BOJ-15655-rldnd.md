# [[BOJ] N과 M(6)](https://www.acmicpc.net/problem/15655)

> [백트래킹]

## 발상

- 써야 하는 값들을 정렬하고 난 뒤, 백트래킹 쓰기

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
arr = sorted(list(map(int, readline().split())))
used = [False] * N
answer = [0] * M

def back_tracking(idx):
    if idx == M:
        return print(*answer)
    for i in range(N):
        if not used[i] and (idx == 0 or (idx > 0 and answer[idx - 1] < arr[i])):
            answer[idx] = arr[i]
            used[i] = True
            back_tracking(idx + 1)
            used[i] = False

back_tracking(0)
```
