# [[BOJ] {듣보잡}](<(https://www.acmicpc.net/problem/1764)>)

> [구현]

> 집합

## 발상

> 교집합 사용

## <br>정답 코드

```python
N, M = list(map(int, input().split()))

listens = set()

for _ in range(N):
    listens.add(input())


seens = set()
for _ in range(M):
    seens.add(input())

together = list(listens.intersection(seens))
together.sort()

print(len(together))
for t in together:
    print(t)

```
