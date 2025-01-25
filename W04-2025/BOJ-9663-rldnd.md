# [[BOJ] N-Queen](https://www.acmicpc.net/problem/9663)

> [브루트포스 알고리즘] [백트래킹]

## 발상

- 놓을 수 있는 위치에 놓고, 백트래킹 사용하기

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 거의 O(N^4)를 넘는 지경의 시간복잡도를 가지다 보니 SIGTERM이 발생한다.
- 전체를 순환하는 방식이 아닌, 수직, 대각선 2개로만 체크해보자.

```python
import sys
readline = sys.stdin.readline

N = int(readline())

board = [[0] * N for _ in range(N)]
used = [[False] * N for _ in range(N)]

answer = 0

"""
queen은 수평, 수직, 대각선 방향으로 모두 놓을 수 있다.
"""
def back_tracking(count):
    global answer

    if count == N:
       answer += 1
       return

    for i in range(N):
        for j in range(N):
            has_used = False
            if used[i][j]:
                break
            for a in range(N):
                if used[i][a] or used[a][j]:
                    has_used = True
                    break
                elif (i - a >= 0 and j - a >= 0 and used[i - a][j - a]) or (i + a < N and j + a < N and used[i + a][j + a]) or (i - a >= 0 and j + a < N and used[i-a][j+a]) or (i+a<N and j-a >=0 and used[i+a][j-a]):
                    has_used = True
                    break
            if not has_used:
                used[i][j] = True
                back_tracking(count + 1)
                used[i][j] = False


back_tracking(0)
print(answer)
```

## <br>정답 코드

- 진짜 어렵다..ㅋㅋㅋ

```python
import sys
readline = sys.stdin.readline

N = int(readline())

used_col = [False] * N # x
used_right_up = [False] * (2 * N - 1) # x + y => x + y가 같으면 같은 대각선
used_left_up = [False] * (2 * N - 1) # x - y + N - 1 => x - y가 같으면 같은 대각선

answer = 0

def back_tracking(row):
    global answer

    if row == N:
        answer += 1
        return
    for col in range(N):
        if used_col[col] or used_right_up[row + col] or used_left_up[col - row + N - 1]:
            continue
        used_col[col] = True
        used_right_up[row + col] = True
        used_left_up[col - row + N - 1] = True
        back_tracking(row + 1)
        used_col[col] = False
        used_right_up[row + col] = False
        used_left_up[col - row + N - 1] = False

back_tracking(0)
print(answer)
```
