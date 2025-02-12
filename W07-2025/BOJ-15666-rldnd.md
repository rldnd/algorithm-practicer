# [[BOJ] N과 M (12)](https://www.acmicpc.net/problem/15666)

> [백트래킹]

## 발상

- 단순 백트래킹

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
A = sorted(list(map(int, readline().split())))

answer = []

def back_tracking(numbers, idx, lst):
    global answer

    if idx == M:
        answer.append(lst[:])
        return
    for i in range(len(numbers)):
        lst[idx] = numbers[i]
        back_tracking(numbers[i:], idx + 1, lst)

back_tracking(A, 0, [0 for _ in range(M)])

answer = sorted(list(set(map(tuple,answer))))
for a in answer:
    print(*a)
```
