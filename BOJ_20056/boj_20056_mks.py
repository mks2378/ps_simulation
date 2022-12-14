import sys; input = sys.stdin.readline

dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    y, x, m, s, d = list(map(int, input().split()))
    board[y-1][x-1].append([m, s, d])

# y, x, m, s, d
for _ in range(K):
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for cy in range(N):
        for cx in range(N):
            if board[cy][cx]:
                for m, s, d in board[cy][cx]:
                    ny = (cy + dy[d] * s) % N
                    nx = (cx + dx[d] * s) % N
                    new_board[ny][nx].append([m, s, d])

    for cy in range(N):
        for cx in range(N):
            if new_board[cy][cx]:
                ball_cnt = len(new_board[cy][cx])
                if ball_cnt>1:
                    nm = sum([row[0] for row in new_board[cy][cx]])//5
                    if nm == 0:
                        new_board[cy][cx].clear()
                    elif nm > 0:
                        ns = sum([row[1] for row in new_board[cy][cx]])//ball_cnt

                        b_odd, b_even = True, True
                        for _, _, d in new_board[cy][cx]:
                            if d%2 == 1:
                                b_even = False
                            else:
                                b_odd = False

                        if b_even == True or b_odd == True:
                            nd_list = [0, 2, 4, 6]
                        else:
                            nd_list = [1, 3, 5, 7]

                        new_board[cy][cx].clear()
                        for nd in nd_list:
                            new_board[cy][cx].append([nm, ns, nd])

    board = new_board

answer = 0
for cy in range(N):
    for cx in range(N):
        if board[cy][cx]:
            answer += sum([row[0] for row in board[cy][cx]])
print(answer)
