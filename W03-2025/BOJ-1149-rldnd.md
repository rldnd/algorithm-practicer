# [[BOJ] RGB거리](https://www.acmicpc.net/problem/1149)

> [DP]

## 발상

- 경험해 보지 않아서 진짜 보이지 않는 내용이었지만, DP를 위해 값을 저장해두는 배열은 꼭 1차원은 아니라는 것이다.
- DP를 2차원으로 해결할 수 있다고 생각해보면, 생각보다 쉬운 내용.

## <br>정답 코드

- 현재의 집이 R이라면 전집의 G, B의 최소값 + 현재의 R 비용.
- 나머지도 다 같은 방식이기에 해당 내용 적용

```python
import sys
readline = sys.stdin.readline

N = int(readline())
DP = [[0] * 3 for _ in range(N)]

R, G, B = map(int, readline().split())
DP[0] = [R, G, B]

for i in range(1, N):
    R, G, B = map(int, readline().split())
    DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + R
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + G
    DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + B

print(min(DP[N - 1]))
```
