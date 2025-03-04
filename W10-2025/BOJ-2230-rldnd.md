# [[BOJ] 수 고르기](https://www.acmicpc.net/problem/2230)

> [정렬] [투 포인터]

## 발상

- 투 포인터 연습해보기

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
A = sorted([int(readline()) for _ in range(N)])

diff = float('inf')
start = 0
end = 1

while end < N and start < N:
    _diff = A[end] - A[start]
    if M <= _diff:
        diff = min(diff, _diff)
        start += 1
    else:
        end += 1

print(diff)
```
