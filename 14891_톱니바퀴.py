from re import L
import sys
circle = []

def rotation(str, dir):
    length = len(str)
    if dir == -1: #ccw
        indx_0 = str[0]
        for i in range(length-1):
            str[i] = str[i+1]
        str[length-1] = indx_0
    else: #cw
        indx_l = str[length-1]
        for i in range(length-1, 0, -1):
            str[i] = str[i-1]
        str[0] = indx_l
    return str

for i in range(4):
    input = sys.stdin.readline().rstrip()
    circle.append(list(input))

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    circle_idx, dir = map(int, sys.stdin.readline().rstrip().split())
    circle_idx -= 1
    if circle_idx == 0:
        if circle[0][2] != circle[1][6]:
            if circle[1][2] !=circle[2][6]:
                if circle[2][2] != circle[3][6]:
                    rotation(circle[3], dir *-1)
                rotation(circle[2], dir)
            rotation(circle[1], dir*-1)
        rotation(circle[0], dir)
    elif circle_idx == 1:
        if circle[0][2] != circle[1][6]:
            rotation(circle[0], dir * -1)
        if circle[1][2] != circle[2][6]:
            if circle[2][2] != circle[3][6]:
                rotation(circle[3], dir)
            rotation(circle[2], dir * -1)
        rotation(circle[1], dir)
    elif circle_idx == 2:
        if circle[1][2] != circle[2][6]:
            if circle[0][2] != circle[1][6]:
                rotation(circle[0], dir)
            rotation(circle[1], dir * -1)
        if circle[2][2] != circle[3][6]:
            rotation(circle[3], dir * -1)
        rotation(circle[2], dir)
    elif circle_idx == 3:
        if circle[2][2] != circle[3][6]:
            if circle[1][2] != circle[2][6]:
                if circle[0][2] != circle[1][6]:
                    rotation(circle[0], dir * -1)
                rotation(circle[1], dir)
            rotation(circle[2], dir * -1)
        rotation(circle[3], dir)



res = 0
for i in range(4):
    north = circle[i][0] #12시에 있는 극
    if north =='1':
        if i ==0:
            res += 1
        elif i ==1:
            res += 2
        elif i ==2:
            res += 4
        else:
            res +=8
print(res)