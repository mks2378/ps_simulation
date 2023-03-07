import sys; input = sys.stdin.readline
from collections import deque

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def InBoard(y, x):
    return 0 <= y < N and 0 <= x < N


def Find_Passenger(sy, sx):
    visited = [[-1]*N for _ in range(N)]
    q = deque([(sy, sx)])
    visited[sy][sx] = 0

    candidates = []
    while q:
        cy, cx = q.popleft()
        # if (cy, cx) in passenger_start:
        #     candidates.append((visited[cy][cx], cy, cx))

        for idx, (ps_sy, ps_sx) in enumerate(passenger_start):
            if (cy, cx) == (ps_sy, ps_sx):
                candidates.append((visited[cy][cx], cy, cx, idx))
                break
        else:
            for d in range(4):
                ny, nx = cy + dy[d], cx + dx[d]
                if InBoard(ny, nx) and board[ny][nx]!=1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[cy][cx] + 1
                    q.append((ny, nx))

    if candidates:
        candidates.sort()
        return candidates[0][0], candidates[0][1], candidates[0][2], candidates[0][3]
    else:
        return -1, -1, -1, -1


def Find_Destination_Dist(py, px, trg_y, trg_x):
    visited = [[-1] * N for _ in range(N)]
    q = deque([(py, px)])
    visited[py][px] = 0
    while q:
        cy, cx = q.popleft()
        if (cy, cx) == (trg_y, trg_x):
            return visited[cy][cx], cy, cx
        else:
            for d in range(4):
                ny, nx = cy + dy[d], cx + dx[d]
                if InBoard(ny, nx) and board[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[cy][cx] + 1
                    q.append((ny, nx))
    return -1, -1, -1


# main
N, M, Fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ty, tx = map(lambda x: int(x)-1, input().split())

passenger_start = []
passenger_end = []
for _ in range(M):
    ps_sy, ps_sx, ps_ey, ps_ex = map(lambda x: int(x)-1, input().split())
    passenger_start.append([ps_sy, ps_sx])
    passenger_end.append([ps_ey, ps_ex])

for _ in range(M):
    pd_dist, py, px, pidx = Find_Passenger(ty, tx)

    if pd_dist == -1 or Fuel - pd_dist < 0:
        Fuel = -1
        break
    else:
        Fuel-=pd_dist
        passenger_start[pidx] = [-1, -1]

    target_y, target_x = passenger_end[pidx]
    dest_dist, dest_y, dest_x = Find_Destination_Dist(py, px, target_y, target_x)

    if dest_dist == -1 or Fuel - dest_dist < 0:
        Fuel = -1
        break
    else:
        Fuel += dest_dist

    # taxi position update
    ty, tx = dest_y, dest_x

print(Fuel)
