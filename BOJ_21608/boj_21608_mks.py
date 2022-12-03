import sys; input = sys.stdin.readline

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

# main
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N**2)]

board = [[0]*N for _ in range(N)]

for student in lst:
    st_num, st_lst = student[0], student[1:]

    candidates = []  # lover, space, cy, cx
    for cy in range(N):
        for cx in range(N):
            lover = 0
            space = 0
            if board[cy][cx] == 0:
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]
                    if 0<=ny<N and 0<=nx<N:
                        if board[ny][nx] in st_lst:
                            lover += 1
                        elif board[ny][nx] == 0:
                            space += 1
                candidates.append([lover, space, cy, cx])

    candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    _, _, y, x = candidates[0]
    board[y][x] = st_num

answer = 0
for student in lst:
    st_num, st_lst = student[0], student[1:]
    cnt = 0
    for cy in range(N):
        for cx in range(N):
            if board[cy][cx] == st_num:
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]
                    if 0<=ny<N and 0<=nx<N and board[ny][nx] in st_lst:
                        cnt+=1
                break
    
    if cnt == 1:
        answer+=1
    elif cnt == 2:
        answer+=10
    elif cnt == 3:
        answer+=100
    elif cnt == 4:
        answer+=1000

print(answer)
