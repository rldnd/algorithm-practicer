# [[BOJ] 수 찾기](https://www.acmicpc.net/problem/1920)

> [자료 구조] [정렬] [이분 탐색] [해시를 사용한 집합과 맵]

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N = int(readline())
A = sorted(list(map(int, readline().split())))
M = int(readline())

targets = list(map(int, readline().split()))

for i in range(M):
    start, end = 0, N - 1
    target = targets[i]
    has_target = False
    while start <= end:
        mid = (start + end) // 2
        if A[mid] < target:
            start = mid + 1
        elif A[mid] > target:
            end = mid - 1
        else:
            has_target = True
            break
    print(1) if has_target else print(0)

```
