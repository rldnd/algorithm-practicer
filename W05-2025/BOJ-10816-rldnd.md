# [[BOJ] 숫자 카드 2](https://www.acmicpc.net/problem/10816)

> [자료 구조] [정렬] [이분 탐색] [해시를 사용한 집합과 맵]

## 발상

- 이분탐색 left의 경우, 해당 target의 제일 왼쪽 index, right의 경우 제일 오른쪽 index를 리턴함.
- 만약 타겟이 없는 경우 right - left + 1을 하게 되면 0이 나오고, 있다면 있는 개수만큼 return

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N = int(readline())
numbers = sorted(list(map(int, readline().split())))

M = int(readline())
finding_numbers = list(map(int, readline().split()))

def bisect_left(target):
    global numbers
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def bisect_right(target):
    global numbers
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right

for finding_number in finding_numbers:
    left, right = bisect_left(finding_number), bisect_right(finding_number)
    print(max(right - left + 1, 0), end = " ")
```
