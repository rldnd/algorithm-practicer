# [[BOJ] 알파벳](https://www.acmicpc.net/problem/1987)

> [그래프 이론] [그래프 탐색] [깊이 우선 탐색] [백트래킹]

## 발상

- DFS 사용

## <br>정답 코드

- ord를 통해 아스키로 변환 가능..!

```python
import sys
readline = sys.stdin.readline

visited = [False] * 26

R, C = map(int, readline().split())

graph = [list(readline()) for _ in range(R)]
visited[ord(graph[0][0]) - 65] = True

nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]

answer = 1

def dfs(r, c, time):
    global answer

    for i in range(4):
        dy = r + ny[i]
        dx = c + nx[i]
        if dy >= 0 and dy < R and dx >= 0 and dx < C and not visited[ord(graph[dy][dx]) - 65]:
            visited[ord(graph[dy][dx]) - 65] = True
            dfs(dy, dx, time + 1)
            visited[ord(graph[dy][dx]) - 65] = False
        else:
            answer = max(answer, time)

dfs(0, 0, 1)
print(answer)
```
