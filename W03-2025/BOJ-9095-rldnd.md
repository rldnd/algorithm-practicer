# [[BOJ] 1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)

> [DP]

## <br>정답 코드

- 사실 DP문제임을 알고 풀어서, 점화식을 만들어내려 해봤지만 왜 DP인지 이해가 가지 않는다.
- DP[N] = DP[N - 1] + DP[N - 2] + DP[N - 3] 으로 점화식이 귀결된다.
- 아래와 같은 이유라고 하는데, 바로 찾지를 못해서 연습을 더 해봐야할 듯 하다.

> [!NOTE]
>
> D[4] = ?
>
> 1+1+1+`1`, 3+`1`, 2+1+`1`, 1+2+`1` (3을 1, 2, 3의 합으로 나타내는 방법)+ 1, D[3]
>
> 1+1+`2`,2+`2` (2를 1,2, 3의 합으로 나타내는 방법) + 2, D[2]
>
> 1+`3` (1을 1, 2, 3의 합으로 나타내는 방법) + 3, D[1]
>
> D[4]=D[1]+D[2]+D[3]

```python
import sys
readline = sys.stdin.readline

T = int(readline())
DP = [0] * 13
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4, 13):
    DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]

for i in range(T):
    print(DP[int(readline())])
```
