# [[BOJ] 설탕 배달](https://www.acmicpc.net/problem/2839)

> [수학] [다이나믹 프로그래밍] [그리디 알고리즘]

## 발상

- 봉지의 최소 개수는 3kg, 5kg 중 사용할 수 있는 5kg 봉지를 최대한 많이 사용할 경우일 것이다.
- 5kg 봉지를 최대한 사용할 수 있는 상태에서 3kg, 5kg 의 배수만으로 표현할 수 있는지 확인한다.
- 표현할 수 없다면 5kg 봉지가 음수가 될 때까지 봉지의 수를 줄여가며 확인한다.

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N = int(readline())

five = N // 5

while five >= 0:
    if not (N - five * 5) % 3:
        print(five + (N - five * 5) // 3)
        break
    else:
        five -= 1

if five < 0:
    print(-1)
```
