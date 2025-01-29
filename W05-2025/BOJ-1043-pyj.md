# [[BOJ] 거짓말](https://www.acmicpc.net/problem/1043)

> [BFS]

## 발상

> 일단 지민이가 같은 파티에 들어가면 안되는 사람의 목록을 만들어야함

## <br>정답 코드

```python
from collections import deque

N, M = list(map(int, input().split()))
truth = list(map(int, input().split()))
party = [[] for i in range(M + 1)]
people = [[] for i in range(N + 1)]


for i in range(1, M + 1):
    p = list(map(int, input().split()))[1:]
    party[i] = p
    for l in p:
        people[l].append(i)


if truth[0] == 0:
    print(M)
    exit()


realTruthList = [*truth[1:]]
queue = deque(truth[1:])
visited = [False] * (M + 1)

while queue:
    c = queue.popleft()

    for part in people[c]:

        if not visited[part]:
            visited[part] = True
            for person in party[part]:
                if person not in realTruthList:
                    realTruthList.append(person)
                    queue.append(person)


answer = 0
for part in party[1:]:
    union = set(part).intersection(set(realTruthList))

    if len(union) == 0:
        answer += 1
print(answer)

```
