import sys
input = sys.stdin.readline

n,m,k = map(int, input().split()) # n 격자 크기 , m 플레이어 수, k 라운드 수
graph = [list(map(int, input().split())) for _ in range(n)]
person = [list(map(int, input().split())) for _ in range(m)]
# 총 여러개 일수도 있음
graph = [[[gr] for gr in gra] for gra in graph]
# index 재배치 + 총 인벤토리 확장(0 추가)
person = [[per[0]-1, per[1]-1, per[2], per[3], 0] for per in person]
person_point = [0 for _ in range(m)]
#상 우 하 좌
dy=[0, 1, 0, -1]
dx=[-1, 0, 1, 0]
def isInside(x,y):
    return 0<=x<n and 0<=y<n
#총 없는 곳에 플레이어 위치

#1-1 첫번째 플레이어 부터 바라보는 방향으로 한칸 이동, 밖으로 나갈시에 방향 바꿔서 한칸 이동
def move_person(p_id):
    x,y,d,_, _= person[p_id]
    nx, ny= x + dx[d], y + dy[d]
    if isInside(nx,ny):
        person[p_id][0], person[p_id][1] = nx, ny
    else:
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d]
        person[p_id][0], person[p_id][1], person[p_id][2] = nx, ny, d

def check_next_graph(p_id):
    x, y, d, s, gun_p = person[p_id]
    ori_per_idx = -1
    b_person = False
    for i in range(len(person)):
        if i == p_id:
            continue
        else:
            # 2-2-1 이동한 방향에 플레이어 있으면 초기 능력 + 총 공격 합 높은사람이 이김, 같으면 -> 초기 능력이 높은 사람이 승리
            if x == person[i][0] and y == person[i][1]:
                ori_per_idx = i
                b_person=True
            else:
                # 2-1 이동한 방향에 플레이어 없으면 -> 해당칸에 총이 있으면 총 획득,
                # 이미 총 갖고 있으면 더 쌘 총 획득,
                # 나머지 총은 격자에 두기
                #이동한 방향에 플레이어 없을 경우
                pass

    if b_person:
        #사람 있을때
        i = ori_per_idx
        # 이동한 방향에 플레이어 있을 경우 #초기 능력 + 총의 공격력 비교
        new_per = s + gun_p
        ori_per = person[i][3] + person[i][4]
        if new_per > ori_per:
            lose_person(i)
            win_person(p_id, new_per - ori_per)
        elif new_per < ori_per:
            lose_person(p_id)
            win_person(i, ori_per - new_per)
        else:
            if s > person[i][3]:
                lose_person(i)
                win_person(p_id, 0)
            elif s < person[i][3]:
                lose_person(p_id)
                win_person(i, 0)
    else:
        if len(graph[x][y]) != 0:
            max_g = sorted(graph[x][y])[-1]  # 가장 큰거
            if gun_p < max_g:
                # 총 줍기
                person[p_id][4] = max_g
                graph[x][y].remove(max_g)
                # 총놓기
                if gun_p != 0:
                    graph[x][y].append(gun_p)


def win_person(p_id, p_diff):
    # 승리한 사람이 초기 능력+ 총의 공격력 합의 차이만큼 포인트 획득
    person_point[p_id] += p_diff
    # 2-2-3 이긴 플레이어는 승리한 칸에 떨어져있는 총들, 들고있는 총들중 가장 높은 공격력 총 획득, 나머지는 격자에 두기
    x, y, d, s, gun_p = person[p_id]
    if len(graph[x][y]) != 0:
        max_g = sorted(graph[x][y])[-1]  # 가장 큰거
        if gun_p < max_g:
            # 총 줍기
            person[p_id][4] = max_g
            graph[x][y].remove(max_g)
            # 총놓기
            if gun_p != 0:
                graph[x][y].append(gun_p)

# 2-2-2 진플레이어는 총 해당 격자에 내려 놓기, 가던 방향으로 한칸 이동, 이때 그 칸에 플레이어 있거나 격자 밖이면 오른쪽 90도로 꺽기(시계방향)
# 꺽어서 이동한 격자에 또 총이 있으면 가장 공격력 높은 총 획득, 나머지 총 격자에 내려놓기
def lose_person(p_id):
    x, y, d, s, gun_p = person[p_id]
    #진플레이어는 총 해당 격자에 내려 놓기
    person[p_id][4] = 0
    if gun_p != 0:
        graph[x][y].append(gun_p)
    #가던 방향으로 한칸 이동, 이때 그 칸에 플레이어 있거나 격자 밖이면 오른쪽 90도로 꺽기(시계방향)
    nx, ny = x + dx[d], y + dy[d]
    while 1:
        b_person = False
        for i in range(len(person)):
            if i == p_id:
                continue
            else:
                if nx == person[i][0] and ny == person[i][1]:
                    b_person = True
        if not isInside(nx, ny) or b_person:
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]
        else:
            break
    # if not isInside(nx, ny) or b_person:
    #     d = (d-1)%4
    #     nx, ny = x + dx[d], y + dy[d]
    #     if not isInside(nx,ny) or b_person:
    #         d = (d - 1) % 4
    #         nx, ny = x + dx[d], y + dy[d]
    person[p_id][2] = d
    person[p_id][0], person[p_id][1] = nx, ny
    # 이동한 격자에 또 총이 있으면 가장 공격력 높은 총 획득, 나머지 총 격자에 내려놓기
    x, y, d, s, gun_p = person[p_id]
    if len(graph[x][y]) != 0:
        max_g = sorted(graph[x][y])[-1]  # 가장 큰거
        #if gun_p < max_g:
        # 총 줍기
        person[p_id][4] = max_g
        graph[x][y].remove(max_g)
        # # 총놓기
        # if gun_p != 0:
        #     graph[x][y].append(gun_p)

def arrange_per():
    per_graph = [[99 for _ in range(n)] for _ in range(n)]
    for i, per in enumerate(person):
        px, py, _ ,_,_ = per
        per_graph[px][py] = i
    return per_graph
def main():
    for cnt in range(k):
        for i in range(len(person)):
            #per_graph = arrange_per()
            move_person(i)
            #per_graph = arrange_per()
            check_next_graph(i)
            #per_graph = arrange_per()

    for pt in person_point:
        print(pt, end=" ")

main()