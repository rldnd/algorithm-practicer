# [[BOJ] N과 M (9)](https://www.acmicpc.net/problem/15663)

> [백트래킹]

## 발상

- 백트래킹을 쓴다.
- 이후 중복된 값들을 지우고 sorting을 진행한다.

## <br>정답 코드

- answers = sorted(list(set(map(tuple, answers)))) 과 같이 중복되는 배열들을 제거할 수 있다는 사실을 알게됨

```python
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
arr = sorted(list(map(int, readline().split())))

answers = []

answer = [0] * M
used = [False] * N

def back_tracking(idx):
    if idx == M:
        return answers.append(answer[:])
    for i, value in enumerate(arr):
        if not used[i]:
            used[i] = True
            answer[idx] = value
            back_tracking(idx + 1)
            used[i] = False

back_tracking(0)

answers = sorted(list(set(map(tuple, answers))))

for a in answers:
    print(*a)
```
