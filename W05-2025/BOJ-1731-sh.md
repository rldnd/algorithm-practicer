# [[BOJ] 최단경로](https://www.acmicpc.net/problem/1753)

> [다익스트라 알고리즘] [큐]

## 발상

- 우선순위큐(heapq:최소힙)를 이용해서 정점과 최단 거리를 구한다

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 시간 초과가 계속 떴는데 pypy로는 맞는 걸 발견하고 입력 부분의 시간을 최소화해줬다.  

```python
import heapq

V, E = map(int,input().split())
K = int(input())

adj = [[]*i  for i in range(20005)]

for i in range(E):
    u,v,w = map(int,input().split())
    adj[u].append([v,w])
    

heap_list = []
heapq.heappush(heap_list, [0, K])

min_distance = [987654321 for i in range(V+1)]
min_distance[K] = 0

while len(heap_list)>0:
    d = heapq.heappop(heap_list)
    if not min_distance[d[1]] == d[0]:
        continue
    if len(adj[d[1]])==0:
        continue
    for i in range(len(adj[d[1]])):
        v = adj[d[1]][i][0]
        w = adj[d[1]][i][1]
        if min_distance[v] > d[0] + w:
            min_distance[v] = d[0]+w
            heapq.heappush(heap_list, [d[0]+w, v])
    
                    
for i in range(1, V+1):
    if not min_distance[i]==987654321:
        print(min_distance[i])
    else:
        print("INF")
    
    
```

## <br>정답 코드

```python
import heapq, sys
readline = sys.stdin.readline

V, E = map(int,input().split())
K = int(input())

adj = [[]*i  for i in range(20005)]

for i in range(E):
    u,v,w = map(int,readline().split())
    adj[u].append([v,w])
    

heap_list = []
heapq.heappush(heap_list, [0, K])

min_distance = [987654321 for i in range(V+1)]
min_distance[K] = 0

while len(heap_list)>0:
    d = heapq.heappop(heap_list)
    if not min_distance[d[1]] == d[0]:
        continue
    if len(adj[d[1]])==0:
        continue
    for i in range(len(adj[d[1]])):
        v = adj[d[1]][i][0]
        w = adj[d[1]][i][1]
        if min_distance[v] > d[0] + w:
            min_distance[v] = d[0]+w
            heapq.heappush(heap_list, [d[0]+w, v])
    
                    
for i in range(1, V+1):
    if not min_distance[i]==987654321:
        print(min_distance[i])
    else:
        print("INF")
```