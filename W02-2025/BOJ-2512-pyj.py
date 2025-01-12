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
