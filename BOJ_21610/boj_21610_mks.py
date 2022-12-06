import sys; input = sys.stdin.readline

dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (-1, -1, 0, 1, 1, 1, 0, -1)

ddy = (-1, -1, 1, 1)
ddx = (-1, 1, -1, 1)


# main
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cloud_info = []
for _ in range(M):
    d, s = map(int, input().split())
    cloud_info.append([d-1, s])

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for d, s in cloud_info:

    new_cloud = []
    visited = [[0]*N for _ in range(N)]
    for cy, cx in cloud:
        ny = (cy + dy[d] * s) % N
        nx = (cx + dx[d] * s) % N

        new_cloud.append([ny, nx])

        board[ny][nx] += 1
        visited[ny][nx] = 1

    for cy, cx in new_cloud:
        cnt = 0
        for d in range(4):
            ny = cy + ddy[d]
            nx = cx + ddx[d]
            if 0<=ny<N and 0<=nx<N and board[ny][nx]:
                cnt+=1
        board[cy][cx] += cnt

    cloud = []
    for y in range(N):
        for x in range(N):
            if board[y][x]>=2 and not visited[y][x]:
                board[y][x]-=2
                cloud.append([y, x])

answer = 0
for row in board:
    answer += sum(row)
print(answer)
