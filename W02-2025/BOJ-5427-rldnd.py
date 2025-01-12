import sys
from collections import deque
readline = sys.stdin.readline

test_case_count = int(readline())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_escape_road_count():
    width, height = map(int, readline().split())
    # False는 접근 불가, True는 접근 가능
    building = []
    fires = []
    fire_visit = [[0] * width for _ in range(height)]
    fire_queue = deque()
    start = []
    per_visit = [[0] * width for _ in range(height)]
    per_queue = deque()
    minimum = 1e9

    for i in range(height):
        line = list(readline().rstrip())
        row = []
        for key, char in enumerate(line):
            if char == '#':
                row.append(False)
            else:
                row.append(True)
                if char == '@':
                    start.append((i, key))
                    per_queue.append((i, key))
                    per_visit[i][key] = 1
                if char == '*':
                    fires.append((i, key))
                    fire_queue.append((i, key))
                    fire_visit[i][key] = 1
        building.append(row)

    while fire_queue:
        q_row, q_col = fire_queue.popleft()
        for i in range(4):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                continue
            if building[ny][nx] and not fire_visit[ny][nx]:
                fire_visit[ny][nx] = fire_visit[q_row][q_col] + 1
                fire_queue.append((ny, nx))


    while per_queue:
        q_row, q_col = per_queue.popleft()
        for i in range(4):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny < 0 or ny >= height or nx < 0 or nx >= width:
                minimum = min(minimum, per_visit[q_row][q_col])
                continue
            if building[ny][nx] and (not fire_visit[ny][nx] or per_visit[q_row][q_col] < fire_visit[ny][nx]):
                per_visit[ny][nx] = per_visit[q_row][q_col] + 1
                per_queue.append((ny, nx))

    print(minimum) if minimum != 1e9 else print('IMPOSSIBLE')

for _ in range(test_case_count):
    get_escape_road_count()