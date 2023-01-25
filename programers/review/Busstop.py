# input example
# {{1, 0, 1}, {1, 1, 1}, {1, 1, 1}}
# output
# {{1, 0 ,1}, {2, 1, 2}, {3, 2, 3}}


from collections import deque
example1 = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
example2 = [[0, 0, 0], [0, 1, 1], [1, 1, 1]]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
inf = int(1e9)


def solution(city: list):

    for row in range(len(city)):
        for col in range(len(city[0])):
            if city[row][col] == 1:
                city[row][col] = inf

    for row in range(len(city)):
        for col in range(len(city[0])):
            if city[row][col] == 0:
                bfs(row, col, city)
    return city


def bfs(row, col, city):
    """
    """
    queue = deque()
    queue.append((row, col))

    while (queue):
        row, col = queue.popleft()
        for i in range(4):
            nrow = row+dx[i]
            ncol = col+dy[i]
            if nrow < 0 or ncol < 0 or nrow >= len(city) or ncol >= len(city[0]):
                continue
            if city[nrow][ncol] > city[row][col]+1:
                city[nrow][ncol] = city[row][col]+1
                queue.append((nrow, ncol))
            else:
                continue


solution(example1)
print("🐍 File: review/Busstop.py | Line: 46 | undefined ~ solution(example1)",
      solution(example2))
