# [[BOJ] 회의실 배정](https://www.acmicpc.net/problem/1931)

> [그리디]

## 발상

> 가장 빨리 끝나는 회의를 시작으로 다음 회의를 계속해서 찾으면 된다.

## <br>정답 코드

```python
N = int(input())

meetings = []

for i in range(N):
    meeting = list(map(int, input().split()))
    meeting.reverse()
    meetings.append(meeting)


meetings.sort()
answer = 1
current = 0

for i in range(N - 1):
    if meetings[current][0] <= meetings[i + 1][1]:

        answer += 1
        current = i + 1


print(answer)

```
