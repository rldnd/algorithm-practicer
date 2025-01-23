# [[BOJ] N-Queen](https://www.acmicpc.net/problem/9663)

> [백트래킹]

> 2차원 배열의 압축

## 발상

> 2찬원 배열로 백트래킹을 쓰면 시간초과가 날 거 같아서 1차원으로 처리
> 배열의 index와 값으로 표현 가능

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 기울기로 대각선 체크하니까 시간초과...
> python3는 무조건 시간 초과...

```python
n = int(input())


board = [0] * n
answer = 0


def check(count):
    global board
    for i in range(count):
        # 같은 열 또는 행
        if board[count] == board[i]:
            return False

        # 대각선
        if (abs(count - i) / abs(board[count] - board[i])) == 1:
            return False
    return True


def countQueen(count):
    global answer, n, board

    if count == n:
        answer += 1
        return

    for i in range(n):
        board[count] = i

        if check(count):
            countQueen(count + 1)


countQueen(0)
print(answer)

```

## <br>정답 코드

```python
N = int(input())


board = [0] * N
answer = 0


def check(count):
    global board
    for i in range(count):
        # 같은 열 또는 행
        if board[count] == board[i]:
            return False

        # 대각선
        if abs(count - i) == abs(board[count] - board[i]):
            return False
    return True


def countQueen(count):
    global answer, N, board

    if count == N:
        answer += 1
        return

    for i in range(N):
        board[count] = i

        if check(count):
            countQueen(count + 1)


countQueen(0)
print(answer)

```
