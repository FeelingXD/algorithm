# 공원 산책
def solution(park, routes):
    return move(park, routes)


def findindex(park):
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] == 'S':
                return (y, x)


def move(park, routes):
    dic = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
    current = findindex(park)
    for route in routes:
        valid = True
        op, t = route.split()
        y, x = current
        for i in range(int(t)):
            ny, nx = y+dic[op][0], x+dic[op][1]
            if 0 <= ny < len(park) and 0 <= nx < len(park[0]) and park[ny][nx] != 'X':
                new_current = (ny, nx)
                y, x = ny, nx
            else:
                valid = False
                break
        if valid:
            current = new_current

    return current
