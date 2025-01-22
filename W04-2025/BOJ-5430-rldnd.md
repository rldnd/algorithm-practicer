# [[BOJ] AC](https://www.acmicpc.net/problem/5430)

> [구현] [자료 구조] [문자열] [파싱] [덱]

## 틀린 발상

- 내용을 보면 단순한 구현으로 보인다. 문제의 내용 그대로 구현.

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 시간 초과가 떴다.
- 현재 O(NlogN) ~ O(N^2) 사이 정도의 시간복잡도를 가지고 있어, 간당간당 해 보인다.

```python
"""
R: 뒤집기 -> 수의 순서를 뒤집음
D:버리기 -> 첫번재 수 버리는 함수. 배열이 비어있으면 에러
"""
import sys
from collections import deque
readline = sys.stdin.readline

T = int(readline())

def func():
    functions = list(readline().rstrip())
    arr_len = int(readline())
    arr_str = readline().strip().lstrip('[').rstrip(']')

    arr = deque(list(arr_str.split(',')) if arr_len else [])

    for f in functions:
        if f == 'R':
            arr.reverse()
        if f == 'D':
            if not arr:
                return print('error')
            arr.popleft()

    answer = ','.join(arr) if arr else []
    print(f'[{answer}]')

for i in range(T):
    func()
```

## <br>정답 코드

- 기존 코드의 arr.reverse()의 경우 O(N)의 시간복잡도를 가지고 있기 때문에 시간 초과가 났다고 판단했다.
- reverse()를 쓰는 대신 최후에 한번만 reverse 하는 것으로 구현 방식을 변경했다

```python
"""
R: 뒤집기 -> 수의 순서를 뒤집음
D:버리기 -> 첫번재 수 버리는 함수. 배열이 비어있으면 에러
"""
import sys
from collections import deque
readline = sys.stdin.readline

T = int(readline())

def func():
    functions = list(readline().rstrip())
    arr_len = int(readline())
    arr_str = readline().strip().lstrip('[').rstrip(']')

    arr = deque(list(arr_str.split(',')) if arr_len else [])

    # -1: front / 1: rear
    position = -1
    for f in functions:
        if f == "R":
            position *= -1
        if f == "D":
            if not arr:
                return print('error')
            arr.popleft() if position == -1 else arr.pop()

    arr.reverse() if position == 1 else arr
    answer = ','.join(arr)
    print(f'[{answer}]')

for i in range(T):
    func()
```
