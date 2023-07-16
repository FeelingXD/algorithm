# 바탕화면정리
def solution(wallpaper):
    min_x, max_x, min_y, max_y = -1, -1, -1, -1
    location = []
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                min_x = min(min_x, x) if min_x != -1 else x
                max_x = max(max_x, x)
                min_y = min(min_y, y) if min_y != -1 else y
                max_y = max(max_y, y)
    answer = [min_y, min_x, max_y+1, max_x+1]
    return answer
