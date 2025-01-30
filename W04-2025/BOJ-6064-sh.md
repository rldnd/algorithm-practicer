# [[BOJ] 카잉 달력](https://www.acmicpc.net/problem/6064)

> [수학] [나머지] [최소공배수]

## 발상

- 최소공배수와 방정식을 적절히 섞어서 수학적으로 푼 뒤 구현.

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 시간복잡도를 고려하지 않아서 계속 시간초과, 메모리 초과  

```python
T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    next_x = 1
    next_y = 1
    year = list()
    year_num = 1
    check = False
    while(True):
        if next_x==x and next_y==y:
            print(year_num)
            check = True
            break  
        if next_x==M and next_y==N:
            break  
        year_num = year_num +1       
        next_x = next_x+1
        next_y = next_y +1
        if next_x>M:
            next_x = 1
        if next_y>N:
            next_y = 1
    if not check:
        print(-1)
```

## <br>정답 코드

- 리스트에 저장하거나 일일히 도는 루프 삭제하고 간단한 구현 방식으로 바꿈

```python
import math
T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    max_len =int(M * N / math.gcd(M, N))
    check = False
    max_N = int((max_len + (x -y))/N)+1
    for j in range(max_N):
        if (N *j+ (x -y)*(-1))%M==0:
            check = True
            print(N *j+ (x -y)*(-1)+x)   
            break
    if not check:
        print(-1)
```