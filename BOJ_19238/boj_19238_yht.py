import sys
input = sys.stdin.readline

n, m, oil = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]
taxi_x, taxi_y = map(int, input().split())
taxi = (taxi_x -1, taxi_y -1)
psg_start = []
psg_fin = []

for _ in range(m):
    ps_sx, ps_sy, ps_fx, ps_fy = map(int, input().split())
    psg_start.append((ps_sx-1, ps_sy-1))
    psg_fin.append((ps_fx-1, ps_fy-1))

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def isInside(x,y):
    return 0 <= x < n and 0<= y < n

def select_closest_psg(taxi):
    visited_dist= [[0] * n for _ in range(n)]
    tx, ty = taxi
    q = deque()
    q.append((tx,ty))
    tmp_for_sort = []
    while q:
        x, y = q.popleft()
        if (x,y) in psg_start:
            #손님 찾음
            tmp_for_sort.append((visited_dist[x][y], x, y))
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not isInside(nx, ny):
                    print(nx, ny)
                    continue
                if array[nx][ny] != 1 and visited_dist[nx][ny] != 0:
                    visited_dist[nx][ny] = visited_dist[x][y] +1
                    print(nx, ny)
                    q.append((nx,ny))
    res_dist, res_x, res_y = -1, -1, -1
    if tmp_for_sort:
        tmp_for_sort.srot()
        res_dist, res_x, res_y = tmp_for_sort[0][0], tmp_for_sort[0][1], tmp_for_sort[0][2]
    return res_dist, res_x, res_y

def go_final(psg_start, psg_fin):
    visited_dist = [[0] * n for _ in range(n)]
    tx, ty = psg_start
    q = deque()
    q.append((tx,ty))
    res_dist, res_x, res_y = -1, -1, -1
    while q:
        x, y = q.popleft()
        if (x, y) == psg_fin:
            #손님 도착지 찾음
            res_dist, res_x, res_y = visited_dist[x][y] ,x, y
            break
            #끝
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not isInside(nx,ny):
                    continue
                if array[nx][ny] != 1 and visited_dist[nx][ny] != 0:
                    visited_dist[nx][ny] = visited_dist[x][y] +1
                    q.append((nx,ny))
    return res_dist, res_x, res_y

for _ in range(m):
    print(select_closest_psg((taxi[1], taxi[0])))