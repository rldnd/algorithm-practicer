# [[BOJ] N과 M(3)](https://www.acmicpc.net/problem/15651)

> [백트래킹]

## 발상1

- permutation의 변형으로도 풀 수 있겠다

## <br>정답 코드1

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

def permutation(arr, n):
    answer = []
    if n == 0:
        return []
    if n == 1:
        return [[i] for i in arr]
    for i in range(len(arr)):
        element = arr[i]
        rest = permutation(arr, n - 1)
        for item in rest:
            answer.append([element] + item)
    return answer

for row in permutation(list(range(1, N+1)), M):
    print(*row)
```

## 발상2

- 백트래킹 유형으로 풀 수 있지만, 사용했는지 여부를 체크할 필요가 없다.
- 사실 생각해보니 첫 번째 유형이랑 구현 방식은 다를바는 없지만, 정답을 저장 해놓느냐 안하느냐의 차이인 듯 하다.

## <br>정답 코드2

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())

answer = [0] * M

def back_tracking(idx):
    if idx == len(answer):
        return print(*answer)
    for i in range(1, N + 1):
        answer[idx] = i
        back_tracking(idx + 1)

back_tracking(0)
```
