# [[백준] {숫자야구} - S3](https://www.acmicpc.net/problem/2503)

> [구현]

> 자료구조가 필요없다.

## 발상

> 숫자야구를 할 줄 안다면 쉽게 발상할 수 있다.
> 100부터 999중에 0을 포함하지 않는 서로 다른 수로 구성된 수를 찾는게 중요 (조합은 시간복잡도가 너무 높음)

## <br>정답 코드

> 사실 그냥 멘탈 힐링하려고 풀었읍니다.

```python
N = int(input())
answers = []

for i in range(N):
    answers.append(list(map(int, input().split())))

candidates = [
    str(a)
    for a in range(100, 1000)
    if (
        (str(a)[0] != str(a)[1] and str(a)[0] != str(a)[2] and str(a)[1] != str(a)[2])
        and (str(a)[0] != "0" and str(a)[1] != "0" and str(a)[2] != "0")
    )
]


result = []
for candi in candidates:
    candi = list(candi)
    f, s, t = candi

    isResult = True

    for numb, strike, ball in answers:
        nF, nS, nT = list(str(numb))

        tStrike = 0
        tBall = 0

        if nF == f:
            tStrike += 1

        if nF == s or nF == t:
            tBall += 1

        if nS == s:
            tStrike += 1
        if nS == f or nS == t:
            tBall += 1

        if nT == t:
            tStrike += 1

        if nT == f or nT == s:
            tBall += 1

        if tStrike != strike or tBall != ball:
            isResult = False
            break

    if isResult:
        result.append(candi)

print(len(result))

```
