import sys; input = sys.stdin.readline
from collections import deque

dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)


def inboard(y, x):

    if 0<=y<N and 0<=x<N:
        return True
    else:
        return False

    
def bfs(y, x, color):

    q = deque([[y, x]])

    block_cnt, rainbow_cnt = 1, 0  # 블록 갯수, 무지개블록 갯수
    blocks, rainbows = [[y, x]], []

    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny = cy + dy[d]
            nx = cx + dx[d]

            if inboard(ny, nx) and not visited[ny][nx] and board[ny][nx] == color:
                visited[ny][nx] = 1
                q.append([ny, nx])
                blocks.append([ny, nx])
                block_cnt += 1

            elif inboard(ny, nx) and not visited[ny][nx] and board[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny, nx])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([ny, nx])

    for rby, rbx in rainbows:
        visited[rby][rbx] = 0

    return [block_cnt, rainbow_cnt, blocks+rainbows]


def gravity(board):

    for cy in range(N-2, -1, -1):
        for cx in range(N):
            if board[cy][cx]>-1:
                ry = cy
                while True:
                    if 0<=ry+1<N and board[ry+1][cx] == -2:
                        board[ry+1][cx] = board[ry][cx]
                        board[ry][cx] = -2
                        ry+=1
                    else:
                        break


def counter_rot90(board):

    new_board = [[0]*N for _ in range(N)]
    for idx in range(N):
        new_board[idx] = [row[-1-idx] for row in board]

    return new_board


# main
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

while True:
    visited = [[0]*N for _ in range(N)]
    blocks = []
    for y in range(N):
        for x in range(N):
            if board[y][x]>0 and not visited[y][x]:
                visited[y][x] = 1
                block_info = bfs(y, x, board[y][x])

                if block_info[0]>=2:
                    blocks.append(block_info)

    blocks.sort(reverse=True)

    # 블록 제거 + 점수 더하기
    if not blocks:
        break

    # remove
    for y, x in blocks[0][2]:
        board[y][x] = -2

    answer += blocks[0][0]**2

    # 중력
    gravity(board)

    # 90도 변환
    board = counter_rot90(board)

    # 중력
    gravity(board)

print(answer)
