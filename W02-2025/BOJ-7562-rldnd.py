import sys
from collections import deque
readline = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

test_count = int(readline())

def get_night_move_counts():
    size = int(readline())
    cur_row, cur_col = map(int, readline().split())
    des_row, des_col = map(int, readline().split())

    if cur_row == des_row and cur_col == des_col:
        return print(0)

    visit_count = [[0 for _ in range(size)] for _ in range(size)]
    queue = deque()
    queue.append((cur_row, cur_col))

    while queue:
        q_row, q_col = queue.popleft()
        for i in range(8):
            ny, nx = q_row + dy[i], q_col + dx[i]
            if ny >= size or ny < 0 or nx >= size or nx < 0:
                continue
            if not visit_count[ny][nx] == 0 and visit_count[q_row][q_col] + 1 >= visit_count[ny][nx]:
                continue
            visit_count[ny][nx] = visit_count[q_row][q_col] + 1
            queue.append((ny, nx))

    print(visit_count[des_row][des_col])

for _ in range(test_count):
    get_night_move_counts()