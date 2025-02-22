# [[BOJ] N과 M(2)](<(https://www.acmicpc.net/problem/15650)>)

> [백트래킹]

## 발상

> 1부터 시작해서 넣었다가 빼기를 계속 반복하면 됨

## <br>정답 코드

```python
N, M = list(map(int, input().split()))


def getNums(start, result):
    global M, N
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(i)
        getNums(i + 1, result)
        result.pop()


getNums(1, [])

```
