# [[BOJ] 거짓말](https://www.acmicpc.net/problem/1043)

> [자료 구조] [그래프 이론] [그래프 탐색] [분리 집합]

## 발상

- 일단 문제의 조건을 보면 O(N^4)까지는 풀 수 있다는 것을 생각함.
- 들은 사람과 함께 파티를 참석하는 경우 그 사람도 들은 사람이 됨. 즉 BFS과 같이 처리가 가능할 것이라 판단.
- 들은 사람들을 모두 체크한 뒤에, 그 사람들의 index를 사용하여 party_people (각 파티마다 참석한 사람들) 배열을 순회하여, 사실을 들은 사람이 아무도 없는 파티의 개수를 셈

## <br>정답 코드

```python
import sys
from collections import deque
readline = sys.stdin.readline

"""
N, M <= 50
각 파티의 사람 <= 50
최대 시간복잡도: O(N^4)
실질적으로 BFS? 와 같은 방식으로 처리해야 할 듯
"""
N, M = map(int, readline().split())
per_count, *people = list(map(int, readline().split()))

# False: 거짓말 들은 적 없음, True: 거짓말 들은 적 있음
all_people = [False] * (N + 1)
queue = deque(people)
checked = [False] * (N + 1)

for i in people:
    all_people[i] = True
    checked[i] = True

party_people = [([0] * (N + 1)) for _ in range(M)]

for i in range(M):
    _, *p = list(map(int,readline().split()))
    for j in p:
        party_people[i][j] = 1

while queue:
    person = queue.popleft()
    for party in party_people:
        if party[person]:
            for idx, is_participant in enumerate(party):
                if is_participant and not checked[idx]:
                    checked[idx] = True
                    queue.append(idx)
                    all_people[idx] = True

heard_people = []
answer = 0

for idx, is_heard in enumerate(all_people):
    if idx and is_heard:
        heard_people.append(idx)

for party in party_people:
    has_heard_person = False
    for heard_person in heard_people:
        if party[heard_person]:
            has_heard_person = True
            break

    if not has_heard_person:
        answer += 1


print(answer)
```
