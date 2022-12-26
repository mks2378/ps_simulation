# sol 1)
"""
import sys; input = sys.stdin.readline
from collections import deque


# main
tire = [deque(list(map(int, input().strip()))) for _ in range(4)]
K = int(input())

# tire_index, direction
order = [list(map(int, input().split())) for _ in range(K)]

# 2, -2
for tire_idx, direction in order:
    t1, t2, t3, t4 = 0, 0, 0, 0

    # -1: 반시계, 1: 시계
    # 바퀴 별로 회전 방향 설정
    if tire_idx == 1:
        t1 = direction

        if tire[0][2] != tire[1][-2]:
            t2 = -1 if t1 == 1 else 1
            if tire[1][2] != tire[2][-2]:
                t3 = -1 if t2 == 1 else 1
                if tire[2][2] != tire[3][-2]:
                    t4 = -1 if t3 == 1 else 1

    elif tire_idx == 2:
        t2 = direction
        if tire[0][2] != tire[1][-2]:
            t1 = -1 if t2 == 1 else 1
        if tire[1][2] != tire[2][-2]:
            t3 = -1 if t2 == 1 else 1
            if tire[2][2] != tire[3][-2]:
                t4 = -1 if t3 == 1 else 1

    elif tire_idx == 3:
        t3 = direction
        if tire[2][2] != tire[3][-2]:
            t4 = -1 if t3 == 1 else 1
        if tire[2][-2] != tire[1][2]:
            t2 = -1 if t3 == 1 else 1
            if tire[1][-2] != tire[0][2]:
                t1 = -1 if t2 == 1 else 1

    else:
        t4 = direction
        if tire[3][-2] != tire[2][2]:
            t3 = -1 if t4 == 1 else 1
            if tire[2][-2] != tire[1][2]:
                t2 = -1 if t3 == 1 else 1
                if tire[0][2] != tire[1][-2]:
                    t1 = -1 if t2 == 1 else 1

    # update
    if t1 == 1:
        tire[0].rotate(1)
    else:
        tire[0].rotate(-1)

    if t2 == 1:
        tire[1].rotate(1)
    else:
        tire[1].rotate(-1)

    if t3 == 1:
        tire[2].rotate(1)
    else:
        tire[2].rotate(-1)

    if t4 == 1:
        tire[3].rotate(1)
    else:
        tire[3].rotate(-1)


# total
answer = 0
for i in range(4):
    if tire[i][0] == 1:
        # print(i, 2**i)
        answer += 2**i

print(answer)
"""

# sol 2)
import sys; input = sys.stdin.readline
from collections import deque

# main
tire = [deque(list(map(int, input().strip()))) for _ in range(4)]
K = int(input())

# tire_index, direction
order = [list(map(int, input().split())) for _ in range(K)]

for tire_idx, direction in order:
    tire_idx-=1

    if tire_idx == 0:
        if tire[0][2] != tire[1][6]:
            if tire[1][2] != tire[2][6]:
                if tire[2][2] != tire[3][6]:
                    tire[3].rotate(direction * (-1))
                tire[2].rotate(direction)
            tire[1].rotate(direction * (-1))
        tire[0].rotate(direction)
    elif tire_idx == 1:
        if tire[0][2] != tire[1][6]:
            tire[0].rotate(direction * (-1))
        if tire[1][2] != tire[2][6]:
            if tire[2][2] != tire[3][6]:
                tire[3].rotate(direction)
            tire[2].rotate(direction * (-1))
        tire[1].rotate(direction)
    elif tire_idx == 2:
        if tire[1][2] != tire[2][6]:
            if tire[0][2] != tire[1][6]:
                tire[0].rotate(direction)
            tire[1].rotate(direction * (-1))
        if tire[2][2] != tire[3][6]:
            tire[3].rotate(direction * (-1))
        tire[2].rotate(direction)
    elif tire_idx == 3:
        if tire[2][2] != tire[3][6]:
            if tire[1][2] != tire[2][6]:
                if tire[0][2] != tire[1][6]:
                    tire[0].rotate(direction * -1)
                tire[1].rotate(direction)
            tire[2].rotate(direction * (-1))
        tire[3].rotate(direction)

answer = 0
for i in range(4):
    if tire[i][0] == 1:
        answer += 2**i
print(answer)
