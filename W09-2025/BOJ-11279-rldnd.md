# [[BOJ] 최대 힙](https://www.acmicpc.net/problem/11279)

> [자료 구조] [우선순위 큐]

## 발상

- heapq를 사용하되, heapq는 min heap 방식이기에 tuple을 사용하여 (-x, x)의 형태로 사용

## <br>정답 코드

```python
import sys
import heapq
readline = sys.stdin.readline

max_heap = []

POP_COMMAND = 0

N = int(readline())
for _ in range(N):
    command = int(readline())
    if command == POP_COMMAND:
        if not max_heap:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap, (-1 * command, command))
```
