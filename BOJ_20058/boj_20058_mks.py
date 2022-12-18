import sys; input = sys.stdin.readline
from collections import deque

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

def rot90(ry, rx):
    temp_board = [[0]*grid_length for _ in range(grid_length)]

    for k in range(grid_length):
        temp_board[k] = [row[rx+k] for row in board[ry:ry+grid_length]][::-1]

    for k in range(grid_length):
        board[ry+k][rx:rx+grid_length] = temp_board[k][:]


def check_adjacent_ice():
    new_board = [[k for k in row] for row in board]

    for cy in range(board_length):
        for cx in range(board_length):
            cnt = 0
            for d in range(4):
                ny = cy + dy[d]
                nx = cx + dx[d]
                if 0<=ny<board_length and 0<=nx<board_length and board[ny][nx]:
                    cnt+=1

            if cnt<3 and new_board[cy][cx]:
                new_board[cy][cx]-=1

    return new_board


def bfs():
    visited = [[False]*board_length for _ in range(board_length)]
    max_area = 0

    for y in range(board_length):
        for x in range(board_length):
            if not visited[y][x] and board[y][x]:
                visited[y][x] = True
                q = deque([[y, x]])
                area = 1

                while q:
                    cy, cx = q.popleft()
                    for d in range(4):
                        ny = cy + dy[d]
                        nx = cx + dx[d]
                        if 0<=ny<board_length and 0<=nx<board_length and board[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append([ny, nx])
                            area+=1

                max_area = max(max_area, area)

    return max_area


# main
N, Q = map(int, input().split())
board_length = 2**N
board = [list(map(int, input().split())) for _ in range(board_length)]
L_list = list(map(int, input().split()))

for L in L_list:
    # rot90
    grid_length = 2 ** L
    for i in range(0, board_length, grid_length):
        for j in range(0, board_length, grid_length):
            rot90(i, j)

    # check adjacent ice
    board = check_adjacent_ice()

total_ice = sum([sum(row) for row in board])
max_ice = bfs()

print(total_ice)
print(max_ice)
