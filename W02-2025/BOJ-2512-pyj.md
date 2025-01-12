# [[BOJ] {예산} - S2](https://www.acmicpc.net/problem/2512)

> [이분탐색]

## 발상

> 예산 범위 내에서 최댓값과 최솟값 사이에서 예산을 설정
> 해당 예산이 문제 조건에 부합하는지 확인

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> M이 각 예산보다 작을 경우에 대해서 고려를 하지 않음

```python
N = int(input())

budgets = list(map(int, input().split()))
budgets.sort()

M = int(input())

candis = [x for x in range(min(budgets), max(budgets) + 1)]


def createBudget(t):
    global budgets
    nBudget = []
    for b in budgets:
        if b < t:
            nBudget.append(b)
        else:
            nBudget.append(t)

    return nBudget


answers = []


def binarySearch():
    global candis, M, answers

    start = 0
    end = len(candis) - 1

    while start <= end:
        mid = (start + end) // 2

        nBudget = createBudget(candis[mid])
        sumBudget = sum(nBudget)

        if sumBudget == M:
            answers.append(candis[mid])
            return

        if sumBudget < M:
            answers.append(candis[mid])
            start = mid + 1
        else:
            end = mid - 1


binarySearch()


print(max(answers))

```

## <br>정답 코드

> 위의 예외인 상황의 경우 예산을 준비된 M을 예산을 사용할 곳의 길이로 나눠주면 됨

```python
N = int(input())

budgets = list(map(int, input().split()))
budgets.sort()

M = int(input())

candis = [x for x in range(min(budgets), max(budgets) + 1)]


def createBudget(t):
    global budgets
    nBudget = []
    for b in budgets:
        if b < t:
            nBudget.append(b)
        else:
            nBudget.append(t)

    return nBudget


answers = []


def binarySearch():
    global candis, M, answers

    start = 0
    end = len(candis) - 1

    while start <= end:
        mid = (start + end) // 2

        nBudget = createBudget(candis[mid])
        sumBudget = sum(nBudget)

        if sumBudget == M:
            answers.append(candis[mid])
            return

        if sumBudget < M:
            answers.append(candis[mid])
            start = mid + 1
        else:
            end = mid - 1


binarySearch()
if len(answers) == 0:

    print(M // len(budgets))
else:
    print(max(answers))

```
