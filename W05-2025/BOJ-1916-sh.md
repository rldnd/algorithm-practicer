# [[BOJ] 최소비용 구하기](https://www.acmicpc.net/problem/1916)

> [다익스트라 알고리즘] [우선순위큐]

## 발상

- 우선순위큐(heapq:최소힙)를 이용해서 정점간의 최소비용을 구한다.

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 중복 변수를 실수로 사용해서 계산한 값이 의도대로 출력되지 않았다. 

```python
import sys, heapq
readline = sys.stdin.readline

N = int(input())
M = int(input())

city = [[]* i for i in range(1002)]

for i in range(M):
    u, v, w = map(int, readline().split())
    city[u].append([v,w])
    
s, a = map(int, input().split())

min_cost = [sys.maxsize * i for i in range(1002)]
min_cost[s] = 0

heapq_list = []

heapq.heappush(heapq_list, [0, s])

while(heapq_list):
   d = heapq.heappop(heapq_list)
   weight = d[0]
   c = d[1]
   if not min_cost[c] == weight:
       continue
   if len(city[c])==0:
       continue
   for k in range(len(city[c])):
       a = city[c][k][0]
       w = city[c][k][1]
       if min_cost[a] > weight + w:
           min_cost[a] = weight+w
           heapq.heappush(heapq_list, [weight+w, a])
       

           
print(min_cost[a])        
```

## <br>정답 코드

```python
import sys, heapq
readline = sys.stdin.readline

N = int(input())
M = int(input())

city = [[]* i for i in range(1002)]

for i in range(M):
    u, v, w = map(int, readline().split())
    city[u].append([v,w])
    
start_city, arrive_city = map(int, input().split())

min_cost = [sys.maxsize * i for i in range(1002)]
min_cost[start_city] = 0

heapq_list = []

heapq.heappush(heapq_list, [0, start_city])

while(heapq_list):
   d = heapq.heappop(heapq_list)
   weight = d[0]
   c = d[1]
   if not min_cost[c] == weight:
       continue
   if len(city[c])==0:
       continue
   for k in range(len(city[c])):
       a = city[c][k][0]
       w = city[c][k][1]
       if min_cost[a] > weight + w:
           min_cost[a] = weight+w
           heapq.heappush(heapq_list, [weight+w, a])
           
       

           
print(min_cost[arrive_city])        
```