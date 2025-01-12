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
