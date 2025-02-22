# [[Programmers] 타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)

> [DFS]

## 발상

> 흠, 이거 자체가 주제가 깊이/너비 우선 탐색이라고 되어있지만 처음에는 감이 잘 안왔다.
> 그래프 형태로 생각해보니, 조금은 이해가 가게 되었다.
> 전체 경우를 모두 따져봐야 하기 때문에 dfs recursion 방식으로 진행해봤다.

## <br>정답 코드

```python
def dfs(numbers, value, target, answer):
    if len(numbers) == 1:
        for mul in [-1, 1]:
            if target == (value + (numbers[0] * mul)):
                answer[0] += 1
        return

    for mul in [-1, 1]:
        dfs(numbers[1:], value + (numbers[0] * mul), target, answer)


def solution(numbers, target):
    answer = [0]
    dfs(numbers, 0, target, answer)

    return answer[0]
```
