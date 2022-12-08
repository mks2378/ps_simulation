import sys; input = sys.stdin.readline

# 북, 동, 남, 서
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

# main
N, M = map(int, input().split())
robot = list(map(int, input().split()))

# 0 : 빈 칸, 1 : 벽
board = [list(map(int, input().split())) for _ in range(N)]
cleared = [[0]*M for _ in range(N)]

while True:
    ry, rx, rd = robot
    cleared[ry][rx] = 1

    for d in range(1, 5):
        nd = (rd-d) % 4
        ny = ry + dy[nd]
        nx = rx + dx[nd]
        if board[ny][nx] == 0 and not cleared[ny][nx]:
            robot = [ny, nx, nd]
            break
    else:
        ny, nx = ry + dy[(rd+2)%4], rx + dx[(rd+2)%4]
        if board[ny][nx] == 1:
            break
        else:
            robot = [ny, nx, rd]

answer = 0
for row in cleared:
    answer += sum(row)
print(answer)
