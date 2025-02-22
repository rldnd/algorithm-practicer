# [[BOJ] {사다리 조작} G3](<[문제링크](https://www.acmicpc.net/problem/15684)>)

> [구현]

> Hash, 조합

## 발상

> 사다리를 타고 내려가는 과정을 어떻게 표현할 것인가?
> 특정 가로열과 세로열과 일치하는 가로선이 있으면 이동 후 밑으로 없으면 그냥 밑으로
> 사다리에 배열을 적용하게 되면 머리가 아파질 것으로 예상해서 논리적으로 구현

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 반복문을 3중으로 겹쳐쓰면서 시간초과 발생

```python
from itertools import combinations

N, M, H = list(map(int, input().split()))

lines = []
for i in range(M):
    a, b = list(map(int, input().split()))
    # a : 가로선, b b + 1 : 세로선
    lines.append([a, b, b + 1])


candis = []


for h in range(1, H + 1):
    for n in range(1, N):
        candi = [h, n, n + 1]

        isOk = True
        for a, b, bp in lines:
            # 겹치는 경우
            if h == a and b == n and bp == n + 1:
                isOk = False

            # 연속하는 경우 오른쪽으로
            if h == a and n + 1 == b:
                isOk = False

            if h == a and n == bp:
                isOk = False
        if isOk:
            candis.append(candi)


answer = -1


def sadari(tLines):
    global N, H
    successes = 0

    for i in range(1, N + 1):
        start = i
        currentH = 1
        # print("start : ", i)
        while currentH <= H:
            nextStart = start
            for a, lineOne, lineTwo in tLines:
                if a == currentH and start == lineOne:
                    nextStart = lineTwo
                elif a == currentH and start == lineTwo:
                    nextStart = lineOne

            start = nextStart
            currentH += 1
            # print(start, currentH)
        # print("end :", i)
        if start == i:
            successes += 1

    return successes == N


def start():
    global candis, answer
    for p in range(4):
        crosses = list(combinations(candis, p))

        for cross in crosses:
            testLines = [*lines, *cross]
            # print(testLines)
            result = sadari(testLines)

            if result:

                answer = p
                return


start()
print(answer)

```

## <br>정답 코드

> 가로선을 찾기 위한 방법을 for문이 아닌 hash를 사용해서 구현
> 어차피 가로선은 특정 위치에 하나밖에 없기 때문

```python
from itertools import combinations

N, M, H = list(map(int, input().split()))

lines = []
for i in range(M):
    a, b = list(map(int, input().split()))
    # a : 가로선, b b + 1 : 세로선
    lines.append([a, b, b + 1])


candis = []


for h in range(1, H + 1):
    for n in range(1, N):
        candi = [h, n, n + 1]

        isOk = True
        for a, b, bp in lines:
            # 겹치는 경우
            if h == a and b == n and bp == n + 1:
                isOk = False

            # 연속하는 경우 오른쪽으로
            if h == a and n + 1 == b:
                isOk = False
            # 연속하는 경우 왼쪽으로
            if h == a and n == bp:
                isOk = False
        if isOk:
            candis.append(candi)

answer = -1


def sadari(tLines):

    ladder = {h: {} for h in range(1, H + 1)}
    for h, b1, b2 in tLines:
        ladder[h][b1] = b2
        ladder[h][b2] = b1

    for start in range(1, N + 1):
        current = start
        for h in range(1, H + 1):
            if current in ladder[h]:
                current = ladder[h][current]
        if current != start:
            return False

    return True


def start():
    global candis, answer
    for p in range(4):
        crosses = list(combinations(candis, p))  # N ^ 2

        for cross in crosses:  #
            testLines = [*lines, *cross]

            result = sadari(testLines)  # H

            if result:

                answer = p
                return


start()
print(answer)

```
