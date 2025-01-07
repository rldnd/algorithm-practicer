import heapq

N, M, K = list(map(int, input().split()))

nodes = [[] for i in range(N + 1)]

for i in range(M):
    city1, city2, time = list(map(int, input().split()))
    nodes[city1].append([city2, time])
    nodes[city2].append([city1, time])


start = 1
end = N


def dijkstra():
    global start, N, K, nodes
    distances = [[float("inf")] * (K + 1) for i in range(N + 1)]
    for i in range(K + 1):
        distances[start][i] = 0

    queue = []
    ## 가중치, 포장도로개수, 시작점
    heapq.heappush(queue, [0, 0, start])

    while queue:
        cWeight, cK, cLoc = heapq.heappop(queue)

        if distances[cLoc][cK] < cWeight:
            continue

        for nLoc, nWeight in nodes[cLoc]:
            distance = nWeight + cWeight
            if distance < distances[nLoc][cK]:
                distances[nLoc][cK] = distance
                heapq.heappush(queue, [distance, cK, nLoc])

            if cK < K:
                if cWeight < distances[nLoc][cK + 1]:
                    distances[nLoc][cK + 1] = cWeight
                    heapq.heappush(queue, [cWeight, cK + 1, nLoc])

    return distances


distances = dijkstra()

print(min(distances[end]))
