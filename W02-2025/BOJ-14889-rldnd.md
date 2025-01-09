# [[BOJ] 스타트와 링크](https://www.acmicpc.net/problem/14889)

> [브루트포스 알고리즘] [백트래킹]

## 틀린 발상

- N이 주어진 경우, N/2만큼 combination을 이루어야 한다.
- 이후 N/2명이 이루어진 팀에서, 2명끼리 묶어 그들의 역량을 합산하고, 반대편의 팀도 마찬가지로 진행한다.
- 2중 for문을 사용할 것 같긴 하지만, 다른 방법이 생각나지 않으니 진행.

## <br>틀린 풀이 코드 및 틀린 이유

```python
import sys
readline = sys.stdin.readline

N = int(readline())
S = [list(map(int, readline().split())) for _ in range(N)]

# 이거 itertools 쓰면 되긴 함
def combination(lst, n):
    answer = []
    if n == 0:
        return []
    if n == 1:
        return [[i] for i in lst]
    for i in range(len(lst)):
        element = lst[i]
        rest = combination(lst[i+1:], n-1)
        for item in rest:
            answer.append([element] + item)
    return answer

s_combination = combination([i for i in range(N)], N // 2)

minimum = 1e9
players = [i for i in range(N)]
for combs in s_combination:
    combs_count, rest_count = 0, 0
    rest = list(set([i for i in range(N)]) - set(combs))

    combs_two_combs = combination(combs, 2)
    rest_two_combs = combination(rest, 2)
    for i in range(len(combs_two_combs)):
        [a, b] = combs_two_combs[i]
        [c, d] = rest_two_combs[i]
        combs_count += S[a][b]
        combs_count += S[b][a]
        rest_count += S[c][d]
        rest_count += S[d][c]
    minimum = min(minimum, abs(combs_count - rest_count))

print(minimum)
```

- 시간 초과가 떴다. 사실 예상한 결과이긴 하지만 더 좋은 결과가 뭐가 있는지 잘 모르겠다..ㅎ
- 조합 자체가 O(n^2) 이기 때문에, 2중 for문까지 쓰면 답이 없게 된다.

## <br>정답 코드

> 답을 아직 못 찾겠음..

```python
print("hello world")
```
