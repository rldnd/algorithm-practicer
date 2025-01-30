# [[BOJ] 세 수의 합](https://www.acmicpc.net/problem/2295)

> [자료 구조] [이분 탐색] [해시를 사용한 집합과 맵] [중간에서 만나기]

## 발상

- combination을 사용해서 3개가 가능한 모든 조합을 생각해내고, 3개의 합이 배열에 존재하는지 확인해보자

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

- 메모리 초과 / 시간 초과
- 시간복잡도가 O(N^3logN) 이라서 불가능 하다. 최대 O(N^2logN) 까지 가능함.

```python
import sys
readline = sys.stdin.readline

N = int(readline())
arr = sorted([int(readline()) for _ in range(N)])
answer = [0] * 3

maximum = -1

def bisect(target):
    global arr
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return True
    return False

def back_tracking(idx, head):
    global maximum

    if idx == 3:
        if bisect(sum(answer)):
            maximum = max(sum(answer), maximum)
        return
    for i in range(head, N):
        answer[idx] = arr[i]
        back_tracking(idx + 1, i)


back_tracking(0, 0)
print(maximum)
```

## <br>정답 코드

- 시간복잡도를 O(N^2logN)으로 맞춰야함.
- x와 y를 모두 더해두고, k를 큰 순으로 for문을 돌리며 k-z 중에서 x+y에 값이 존재하는지 확인

```python
import sys
readline = sys.stdin.readline

N = int(readline())
arr = sorted([int(readline()) for _ in range(N)])

xy_sum = []

def bisect(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return True
    return False

for x in range(N):
    for y in range(x, N):
        xy_sum.append(arr[x] + arr[y])

xy_sum.sort()

for k in reversed(range(N)):
    for z in range(N):
        if bisect(xy_sum, arr[k] - arr[z]):
            print(arr[k])
            exit()


```
