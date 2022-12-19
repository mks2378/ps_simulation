import sys; input = sys.stdin.readline


def tornado(ty, tx, direction):
    global answer

    if tx<0:
        return

    total = 0
    for s_dy, s_dx, ratio in direction:
        ny = ty + s_dy
        nx = tx + s_dx

        # 정해진 비율에 따라 모래 양 먼저 구하고, 밖으로 나가는지 판단
        if ratio != 0:
            new_sand = int(board[ty][tx] * ratio)  # round 대신 int 사용
            total += new_sand
        else:
            new_sand = board[ty][tx] - total

        if 0<=ny<N and 0<=nx<N:
            board[ny][nx] += new_sand
        else:
            answer += new_sand

    board[ty][tx] = 0

# main
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 위쪽 방향이 마이너스 방향.
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1), (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(y, -x, z) for y, x, z in left]
up = [(x, y, z) for y, x, z in left]
down = [(-x, y, z) for y, x, z in left]

ty, tx = N//2, N//2
answer = 0
dy = (0, 1, 0, -1)
dx = (-1, 0, 1, 0)
direction = {0:left, 1:down, 2:right, 3:up}

time = 0
for i in range(2*N-1):
    d = i%4
    if d == 0 or d == 2:
        time += 1

    for _ in range(time):
        ty+=dy[d]
        tx+=dx[d]
        tornado(ty, tx, direction[d])

print(answer)
