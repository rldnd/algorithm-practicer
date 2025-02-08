# [[Programmers] 더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)

> [힙]

## 발상

- min heap 쓰기

## <br>정답 코드

```python
import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            break
        least, second = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, least + second * 2)
        answer += 1

    if scoville[0] < K:
        return -1
    return answer
```
