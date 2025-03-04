# [[BOJ] 부분합](https://www.acmicpc.net/problem/1806)

> [누적 합] [투 포인터]

## 발상

- 투포인터를 사용해 누적합과 부분합 수열의 시작 끝 지점을 저장해놓기

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline


"""
길이 N짜리 수열
연속된 수들의 부분합 중에 그 합이 S이상이 되는 것. 즉 가장 짧은 것의 길이.,
"""
N, S = map(int, readline().split())
A = list(map(int, readline().split()))

s, e = 0, 0
summation = A[0]
answer = float('inf')

while e < N and s < N:
    if summation >= S:
        answer = min(answer, e - s + 1)
        if not e == s:
            summation -= A[s]
            s += 1
        else:
            e += 1
            if e < N:
                summation += A[e]
    else:
        e += 1
        if e < N:
            summation += A[e]

print(0) if answer == float('inf') else print(answer)
```
