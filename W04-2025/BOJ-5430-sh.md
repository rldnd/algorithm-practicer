# [[BOJ] AC](https://www.acmicpc.net/problem/5430)

> [자료구조] [문자열]

## 발상

- 스택에 넣었다 꺼냈다 하면 너무 복잡해서 시작점과 끝점, reverse 유무를 저장해두고 마지막에 출력할때 존재하는 값들만 출력해준다

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 배열에 하나만 존재할때 D를 하면 start>finish 문에 조건을 만족하면서 error를 출력한다. 하지만 정답은 빈 배열을 출력해야 한다. 따라서 D 의 개수를 세어 만약 처음 주어진 배열의 개수와 같다면 빈 배열을 출력해주는 조건을 추가해줬다. 

```python
T = int(input())
for i in range(T):
    p = input()
    arr_n = int(input())
    arr = input().replace("[","").replace("]","").split(",")
    if arr_n>0:
        int_arr = list(map(int, arr))
    start = 0
    finish = arr_n-1
    isFront = True
    for k in range(len(p)):
        if p[k]=='R':
            isFront = not isFront
        elif p[k]=='D':
            if isFront:
                start += 1
            else:
                finish -= 1
    if start>finish:
        print("error")
        continue
    if arr_n==0:
        print("[]")
        continue
    if isFront:
        print("[", end="")
        for k in range(start, finish):
            # ','.join(array)
            print(int_arr[k],end=",")
        print(int_arr[finish], end = "]")
        print()
    elif not isFront:
        print("[", end="")
        for k in range(finish, start, -1):
            print(int_arr[k], end=",")
        print(int_arr[start], end="]")
        print()
```

## <br>정답 코드

```python
T = int(input())
for i in range(T):
    p = input()
    arr_n = int(input())
    arr = input().replace("[","").replace("]","").split(",")
    if arr_n>0:
        int_arr = list(map(int, arr))
    del_sum = 0
    start = 0
    finish = arr_n-1
    isFront = True
    for k in range(len(p)):
        if p[k]=='R':
            isFront = not isFront
        elif p[k]=='D':
            del_sum += 1
            if isFront:
                start += 1
            else:
                finish -= 1
    if del_sum==arr_n:
        print("[]")
        continue
    if start>finish:
        print("error")
        continue
    if arr_n==0:
        print("[]")
        continue
    if isFront:
        print("[", end="")
        for k in range(start, finish):
            # ','.join(array)
            print(int_arr[k],end=",")
        print(int_arr[finish], end = "]")
        print()
    elif not isFront:
        print("[", end="")
        for k in range(finish, start, -1):
            print(int_arr[k], end=",")
        print(int_arr[start], end="]")
        print()
```