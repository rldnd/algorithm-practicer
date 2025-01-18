# [[BOJ] {카잉 달력} - S1](문제링크)

> [구현]

## 발상

> 특정 연도를 m,n,x,y의 조합으로 만들 수 있는지 여부를 파악

## <br>정답 코드

```python
def getYear(m, n, x, y):
    year = x

    while year <= m * n:
        if (year - x) % m == 0 and (year - y) % n == 0:
            return year
        year += m
    return -1


T = int(input())

for _ in range(T):
    m, n, x, y = map(int, input().split())

    print(getYear(m, n, x, y))

```
