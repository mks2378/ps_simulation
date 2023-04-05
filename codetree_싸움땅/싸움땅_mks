EMPTY = (-1, -1, -1, -1, -1, -1)

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

# (y, x)가 격자 벗어나는지 여부 확인
def in_range(y, x):
    return 0 <= y < N and 0 <= x < N


# 현재 (y, x) 위치에서 방향 d를 보고 있을 때
# 그 다음 위치와 방향을 찾는다.
def get_next(y, x, d):
    ny, nx = y + dy[d], x + dx[d]

    # 격자를 벗어나면 방향 뒤집어 반대 방향으로 한 칸 이동
    if not in_range(ny, nx):
        # 반대 방향
        # d = (d + 2) if d < 2 else (d - 2)
        d = (d + 2) % 4
        ny, nx = y + dy[d], x + dx[d]

    return (ny, nx, d)

# 해당 칸에 있는 player를 찾아줍니다.
# 없다면 EMPTY 반환
def find_player(pos):
    for i in range(M):
        _, y, x, _, _, _ = players[i]
        if pos == (y, x):
            return players[i]

    return EMPTY

# player p의 정보 갱신
def update(p):
    num, _, _, _, _, _ = p

    # player 관리 db에서 해당 플레이어 p를 찾아 값 갱신
    for i in range(M):
        num_i, _, _, _, _, _ = players[i]

        if num_i == num:
            players[i] = p
            break

# 플레이어 p를 pos 위치로 이동시킨다
def move(p, pos):
    num, y, x, d, s, a = p
    ny, nx = pos

    """ 이 부분을 구현 못했다 """
    # 가장 좋은 총으로 갱신
    gun[ny][nx].append(a)
    gun[ny][nx].sort(reverse=True)
    a = gun[ny][nx][0]
    gun[ny][nx].pop(0)

    p = (num, ny, nx, d, s, a)
    update(p)

# 진 사람의 움직임을 진행합니다
# 결투에서 패배한 위치는 pos입니다.
def loser_move(p):
    num, y, x, d, s, a = p

    # 먼저 현재 위치에 총을 내려놓게 된다.
    gun[y][x].append(a)

    # 빈 공간을 찾아 이동
    # 현재 방향에서 시작하여 90도씩 시계방향으로 회전하다가 비어있는 최초의 곳으로 이동
    for i in range(4):
        nd = (d + i) % 4
        ny, nx = y + dy[nd], x + dx[nd]
        if in_range(ny, nx) and find_player((ny, nx)) == EMPTY:
            p = (num, y, x, nd, s, 0)
            move(p, (ny, nx))
            break

# player 1 & 2가 pos에서 만나 결투
def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2
    # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로 우선순위를 매겨 비교

    # p1이 이긴 경우
    """아래처럼 tuple로 순차적 비교하게 구현할 수 있다"""
    if (s1 + a1, s1) > (s2 + a2, s2):
        # p1은 포인트 획득
        points[num1] += (s1 + a1) - (s2 + a2)
        # p2는 진 사람의 움직임 진행
        loser_move(p2)
        # 이후 p1은 이긴 사람의 움직임 진행
        move(p1, pos)
    # p2가 이긴 경우
    else:
        # p2는 포인트 획득
        points[num2] += (s2 + a2) - (s1 + a1)
        # p1은 진 사람의 움직임을 진행
        loser_move(p1)
        # 이후 p2는 이긴 사람의 움직임을 진행
        move(p2, pos)

# 시뮬레이션 진행
def simulate():
    # 첫 번째 플레이어부터 순서대로 진행
    for i in range(M):
        num, y, x, d, s, a = players[i]

        # step 1-1. 현재 플레이어가 움직일 그 다음 위치와 방향을 구한다.
        ny, nx, nd = get_next(y, x, d)

        # 해당 위치에 있는 전 플레이어 정보를 얻는다.
        next_player = find_player((ny, nx))

        # 현재 플레이어 위치와 방향 보정
        cur_player = (num, ny, nx, nd, s, a)
        update(cur_player)

        # step 2. 해당 위치로 이동
        # step 2-1. 해당 위치에 플레이어가 없다면 그대로 움직인다.
        if next_player == EMPTY:
            move(cur_player, (ny, nx))
        else:
            duel(cur_player, next_player, (ny, nx))

# MAIN
# 변수 선언 및 입력:
N, M, K = map(int, input().split())

gun = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(N):
        # 총이 놓여있는 칸
        if nums[j] != 0:
            gun[i][j].append(nums[j])

"""
각 칸마다 플레이어 정보를 관리. 순서대로 (num, y, x, d, s, a) 정보 관리.
(y, x) 위치, 방향 d, 초기 능력치 s, num번 플레이어, 공격력 a 총 소지 의미
"""
players = []
for i in range(M):
    y, x, d, s = map(int, input().split())
    players.append((i, y-1, x-1, d, s, 0))

# up, right, down, left
points = [0] * M

# K번 시뮬레이션
for _ in range(K):
    simulate()

# 정답 출력
for pt in points:
    print(pt, end=' ')
