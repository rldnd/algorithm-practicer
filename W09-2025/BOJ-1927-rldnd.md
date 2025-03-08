# [[BOJ] 최소 힙](https://www.acmicpc.net/problem/1927)

> [자료 구조] [우선순위 큐]

## 발상

- 단순 최소 힙 문제

## <br>정답 코드

```python
import sys
import heapq
readline = sys.stdin.readline

N = int(readline())

arr = []
commands = [int(readline()) for _ in range(N)]

for com in commands:
    if com == 0:
        if not arr:
            print(0)
            continue
        print(heapq.heappop(arr))
        continue
    heapq.heappush(arr, com)

```
