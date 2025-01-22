# [[BOJ] N과 M(5)](https://www.acmicpc.net/problem/15654)

> [백트래킹]

## 발상

> 연속된 수가 아니기 때문에 visited 처피 필요

## <br>정답 코드

```python
N, M = list(map(int, input().split()))
numbs = list(map(int, input().split()))

numbs.sort()
visited = [False] * N


def getNumbs(result):
    global numbs, M, visited

    if len(result) == M:
        print(*result)
        return

    for idx, i in enumerate(numbs):
        if not visited[idx]:
            result.append(i)
            visited[idx] = True
            getNumbs(result)
            result.pop()
            visited[idx] = False


getNumbs([])

```
