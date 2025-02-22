# [[BOJ] {후보 추천하기} - S1](<(https://www.acmicpc.net/problem/1713)>)

> [구현]

> _위와 같이 만약 사용한 알고리즘 기술 및 자료구조가 있다면, 적어주세요._

## 발상

> 추천 받은 학생의 수 와 추천의 개수 그리고 추천을 받은 시점을 기억해야한다.

## <br>정답 코드

```python
N = int(input())
M = int(input())
students = list(map(int, input().split()))

## 사진 틀
pictures = [[] for i in range(M)]

for sIdx, student in enumerate(students):
    student -= 1

    notEmptyPicture = [x for x in pictures if len(x) > 0]
    ## [추천 받은 index,추천수 ]

    ## 이미 추천을 받은 경우
    if len(pictures[student]) > 0:
        pictures[student] = [pictures[student][0], pictures[student][1] + 1]

    ## 새롭게 추가하는 경우
    else:
        ## 액자가 꽉찬 경우
        if len(notEmptyPicture) == N:
            minRecommend = []
            minValue = float("inf")
            for nep in notEmptyPicture:
                if nep[1] < minValue:
                    minValue = nep[1]
                    minRecommend = [nep]
                elif nep[1] == minValue:
                    minRecommend.append(nep)
            minRecommend.sort()
            pIndex = pictures.index(minRecommend[0])
            pictures[pIndex] = []
        pictures[student] = [sIdx, 1]


print(*[idx + 1 for idx, x in enumerate(pictures) if len(x) > 0])

```
