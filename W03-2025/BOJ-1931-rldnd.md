# [[BOJ] 회의실 배정](https://www.acmicpc.net/problem/1931)

> [그리디 알고리즘] [정렬]

## 발상

- 생각하기 좀 많이 어려웠다. 처음에는 시작시간을 기준으로 오름차순 배열 이후, 종료 - 시작시간으로 정렬을 해보았으나 어떻게 해도 처리가 되질 않았다.
- 그렇게 되어 차라리 종료시간을 기준으로 정렬을 한 뒤에, 시작시간으로 정렬을 하게 됨.

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 첫번째 아이템은 무조건 넣어야지 라는 생각만하고, 그 뒤에 continue를 안써서 틀림..

```python
import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline())
times = []

for _ in range(N):
    s, e = map(int, (readline().split()))
    times.append((s, e))

times.sort(key = lambda x: (x[1], x[0]))

"""
제일 빨리 끝나야 한다.
"""

sorted_times = deque()

for key, time in enumerate(times):
    if key == 0:
        sorted_times.append(time)
    if sorted_times[-1][1] > time[0]:
        continue
    sorted_times.append(time)

print(len(sorted_times))
```

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline())
times = []

for _ in range(N):
    s, e = map(int, (readline().split()))
    times.append((s, e))

times.sort(key = lambda x: (x[1], x[0]))

"""
제일 빨리 끝나야 한다.
"""

sorted_times = deque()

for key, time in enumerate(times):
    if key == 0:
        sorted_times.append(time)
        continue

    if sorted_times[-1][1] > time[0]:
        continue
    sorted_times.append(time)

print(len(sorted_times))
```
