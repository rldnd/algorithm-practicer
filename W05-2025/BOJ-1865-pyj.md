# [[BOJ] 웜홀](https://www.acmicpc.net/problem/1865)

> [벨만포드]

## 발상

> 음수의 가중치가 존재하면 벨만포드를 사용

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 거리를 초기화할 때 float("inf")로 하면 음수 가중치를 더해도 무한대로 유지가 됨

```python
import sys

input = sys.stdin.readline

T = int(input())


def dfs(distances, start):
    distances[start] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for nNode, nDist in nodes[j]:
                if distances[nNode] > nDist + distances[j]:
                    distances[nNode] = nDist + distances[j]
                    if i == N:
                        return True
    return False


for _ in range(T):
    N, M, W = list(map(int, input().split()))
    nodes = [[] for i in range(N + 1)]

    # 도로의 정보
    # S,E 연결된 지점
    # T 이동하는데 걸리는 시간
    for m in range(M):
        S, E, T = list(map(int, input().split()))
        nodes[S].append([E, T])
        nodes[E].append([S, T])

    # 웜홀의 정보
    # S 시작
    # E 도착
    # T 줄어드는 시간
    for w in range(W):
        S, E, T = list(map(int, input().split()))
        nodes[S].append([E, -T])

    distances = [float("inf")] * (N + 1)

    answer = dfs(distances, 1)

    if not answer:
        print("NO")
    else:
        print("YES")

```

## <br>정답 코드

```python
import sys

input = sys.stdin.readline

T = int(input())


def dfs(distances, start):
    distances[start] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for nNode, nDist in nodes[j]:
                if distances[nNode] > nDist + distances[j]:
                    distances[nNode] = nDist + distances[j]
                    if i == N:
                        return True
    return False


for _ in range(T):
    N, M, W = list(map(int, input().split()))
    nodes = [[] for i in range(N + 1)]

    # 도로의 정보
    # S,E 연결된 지점
    # T 이동하는데 걸리는 시간
    for m in range(M):
        S, E, T = list(map(int, input().split()))
        nodes[S].append([E, T])
        nodes[E].append([S, T])

    # 웜홀의 정보
    # S 시작
    # E 도착
    # T 줄어드는 시간
    for w in range(W):
        S, E, T = list(map(int, input().split()))
        nodes[S].append([E, -T])

    distances = [10001] * (N + 1)

    answer = dfs(distances, 1)

    if not answer:
        print("NO")
    else:
        print("YES")

```
