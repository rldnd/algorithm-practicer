# [[Programmers] 정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)

> [DP]

## 발상

- 처음으로는 DP 문제이긴 하나, DFS로 처리가 가능할 것 같아서 처리해보려 했다. 하지만 조금 생각을 해보니 recursion error가 날 것 같아서 dp를 사용하기로 했다.
- DP 배열을 triangle과 동일하게 2차원 배열로 만들고, 해당 DP 위치에 방문할 때, maximum으로 갈아 치우면 된다.

## <br>정답 코드

```python
def solution(triangle):
    DP = []
    for i in range(len(triangle)):
        DP.append([0] * (i + 1))

    DP[0][0] = triangle[0][0]

    for i in range(len(DP) - 1):
        for j in range(len(DP[i])):
            DP[i + 1][j] = max(DP[i][j] + triangle[i + 1][j], DP[i + 1][j])
            DP[i + 1][j + 1] = max(DP[i][j] + triangle[i + 1][j + 1], DP[i + 1][j + 1])

    return max(DP[-1])

```
