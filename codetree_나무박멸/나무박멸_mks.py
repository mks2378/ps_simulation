import sys; input = sys.stdin.readline

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

ddy = (1, -1, 1, -1)
ddx = (1, 1, -1, -1)


def grow_up():
    for cy in range(N):
        for cx in range(N):
            if board[cy][cx]>0:
                cnt = 0
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]
                    if 0<=ny<N and 0<=nx<N and board[ny][nx]>0:
                        cnt+=1

                board[cy][cx]+=cnt


def spread_tree():
    new_board = [[k for k in row] for row in board]

    for cy in range(N):
        for cx in range(N):
            if new_board[cy][cx]>0:
                empty_pos = []
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]
                    if 0<=ny<N and 0<=nx<N and new_board[ny][nx] == 0 and remove_board[ny][nx] == 0:
                        empty_pos.append((ny, nx))
                length = len(empty_pos)
                for ey, ex in empty_pos:
                    board[ey][ex] += new_board[cy][cx] // length


def find_remove_center():
    temp = []
    for cy in range(N):
        for cx in range(N):
            if board[cy][cx]>0:
                cnt = board[cy][cx]
                for d in range(4):
                    for k in range(1, K+1):
                        ny = cy + ddy[d] * k
                        nx = cx + ddx[d] * k
                        if 0<=ny<N and 0<=nx<N:
                            if board[ny][nx] == -1 or board[ny][nx] == 0 or remove_board[ny][nx]>0:
                                break
                            elif board[ny][nx]>0:
                                cnt += board[ny][nx]

                temp.append((cnt, cy, cx))

    temp.sort(key=lambda x: (-x[0], x[1], x[2]))
    if not temp:
        return (0, 0, 0)
    return temp[0]


def decrease_remover():
    for cy in range(N):
        for cx in range(N):
            if remove_board[cy][cx]>0:
                remove_board[cy][cx] -= 1


def remove_tree():
    cnt, ry, rx = find_remove_center()
    if cnt == 0:
        return 0

    remove_board[ry][rx] = C
    board[ry][rx] = 0
    for d in range(4):
        for k in range(1, K+1):
            ny = ry + ddy[d] * k
            nx = rx + ddx[d] * k
            if 0<=ny<N and 0<=nx<N:
                if board[ny][nx] == -1:
                    break
                elif board[ny][nx] == 0:
                    remove_board[ny][nx] = C
                    break
                elif board[ny][nx]>0:
                    board[ny][nx] = 0
                    remove_board[ny][nx] = C

    return cnt


# main
N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
remove_board = [[0]*N for _ in range(N)]

answer = 0
for _ in range(M):
    grow_up()

    spread_tree()

    decrease_remover()

    answer += remove_tree()

print(answer)
