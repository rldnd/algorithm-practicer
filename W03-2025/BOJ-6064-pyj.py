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
