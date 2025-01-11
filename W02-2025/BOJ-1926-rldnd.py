import sys
from collections import deque
readline = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

height, width = map(int, readline().split())
base = [list(map(int, readline().split())) for _ in range(height)]
visited = [[False for _ in range(width)] for _ in range(height)]

count = 0
maximum = -1

for row in range(height):
    for col in range(width):
        if visited[row][col] or not base[row][col]:
            continue
        queue = deque()
        queue.append(( row, col ))
        visited[row][col] = True
        count += 1
        area = 0
        while queue:
            area += 1
            queue_row, queue_col = queue.popleft()
            for i in range(4):
                ny, nx = queue_row + dy[i], queue_col + dx[i]
                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue
                if visited[ny][nx] or not base[ny][nx]:
                    continue
                queue.append(( ny, nx ))
                visited[ny][nx] = True
        maximum = max(maximum, area)

print(count)
print(0) if maximum == -1 else print(maximum)