# [[BOJ] 잃어버린 괄호](https://www.acmicpc.net/problem/1541)

> [수학] [그리디 알고리즘] [문자열] [파싱]

## 발상

- 식의 최소가 어떻게 생길지 생각해보자.
- a - b + c - d + e가 있다고 생각했을 때, (b+c), (d+e)를 묶어주면 될 것이다.
- 즉 뺄셈 사이에 있는 모든 값들을 먼저 처리해주고 나서, 맨 앞은 +, 나머지는 -로 누산시키면 된다.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

answer = 0
line = readline().rstrip()

for idx, item in enumerate(line.split('-')):
    value = sum(map(int, item.split('+')))
    if idx == 0:
        answer += value
    else:
        answer -= value

print(answer)
```
