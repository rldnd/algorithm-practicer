# [[BOJ] 2 X n 타일링](https://www.acmicpc.net/problem/11726)

> [DP]

## 발상

> 테이블을 만들어보면, DP[i] = DP[i - 1] + DP[i - 2]의 결과가 나옴.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

n = int(readline())

DP = [0] * 1_001
DP[1] = 1
DP[2] = 2

for i in range(3, 1001):
    DP[i] = (DP[i - 1] + DP[i - 2]) % 10_007

print(DP[n])
```
