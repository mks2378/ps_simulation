import sys; input = sys.stdin.readline
from collections import deque

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

def in_range(y, x):
    return 0<=y<N and 0<=x<N

def bfs(board, visited, y, x):
    group = [(y, x)]
    g_num = board[y][x]

    visited[y][x] = 1
    q = deque([(y, x)])
    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if in_range(ny, nx) and not visited[ny][nx] and g_num == board[ny][nx]:
                group.append((ny, nx))
                visited[ny][nx] = 1
                q.append((ny, nx))

    return group

def get_num_near_line(g1, g2):
    answer = 0
    for g1_y, g1_x in g1:
        for g2_y, g2_x in g2:
            diff = abs(g1_y - g2_y) + abs(g1_x - g2_x)
            if diff == 1:
                answer += 1

    return answer

def get_score(board):
    score = 0
    groups = []
    visited = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                temp_g = bfs(board, visited, y, x)
                groups.append(temp_g)

    num_group = len(groups)
    for i in range(num_group-1):
        for j in range(i+1, num_group):
            g1, g2 = groups[i], groups[j]
            num_near_line = get_num_near_line(g1, g2)
            g1_num = board[g1[0][0]][g1[0][1]]
            g2_num = board[g2[0][0]][g2[0][1]]

            score += (len(g1) + len(g2)) * g1_num * g2_num * num_near_line

    return score

def rotate_board(board):
    new_board = [[0] * N for _ in range(N)]
    HALF = N // 2

    # 가운데 십자가 반시계 90도 회전
    new_board[HALF] = [row[HALF] for row in board]
    for j in range(N):
        new_board[j][HALF] = board[HALF][N-1-j]

    # 십자가 외 4개 부분 각각 시계방향 90도 회전
    for i in range(HALF):
        new_board[i][:HALF] = [row[i] for row in board[:HALF]][::-1]
        new_board[i][HALF+1:] = [row[i+HALF+1] for row in board[:HALF]][::-1]
    for i in range(HALF+1, N):
        new_board[i][:HALF] = [row[i-(HALF+1)] for row in board[HALF+1:]][::-1]
        new_board[i][HALF+1:] = [row[i] for row in board[HALF+1:]][::-1]

    return new_board

# MAIN
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

total = 0

# 초기예술 점수
total += get_score(board)

# 1,2,3 회전 이후 예술 점수 // 회전 수 잘못 체크
for _ in range(3):
    board = rotate_board(board)

    total += get_score(board)

print(total)
