import heapq

N = int(input())
M = int(input())

nodes = [[] for i in range(N + 1)]
"""
nodes
    도시
도시 000
    000
"""
for i in range(M):
    start, end, cost = list(map(int, input().split()))

    nodes[start].append([end, cost])

start, end = list(map(int, input().split()))


def dijkstra(nodes, start):
    global N
    queue = []
    distances = [float("inf")] * (N + 1)
    distances[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        currentW, currentV = heapq.heappop(queue)

        if distances[currentV] < currentW:
            continue

        for newV, newW in nodes[currentV]:
            distance = newW + currentW

            if distance < distances[newV]:
                distances[newV] = distance
                heapq.heappush(queue, [distance, newV])

    return distances


distances = dijkstra(nodes, start)

print(distances[end])
