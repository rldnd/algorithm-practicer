# [[BOJ] {시험 감독} - B2](<(https://www.acmicpc.net/problem/13458)>)

## <br>정답 코드

> 정답률 낮길래 풀었는데 브론즈라니...

```python
import math

N = int(input())
appliers = list(map(int, input().split()))
B, C = list(map(int, input().split()))

main = 0
sub = 0


for a in appliers:
    mainDiff = a - B
    main += 1
    if mainDiff > 0:
        subCount = math.ceil(mainDiff / C)

        sub += subCount

print(main + sub)

```
