# 피로도
def solution(k, dungeons):
    """
    최소 피로도 , 소모 피로도
    """
    global ans, visited, dungeon
    dungeon = dungeons
    visited = [False] * len(dungeons)
    ans = 0
    dfs(0, k)
    print(ans)
    return ans


def dfs(n: int, c_fatigue: int):
    global ans, visited, dungeon
    if n > ans:
        ans = n
    for i in range(len(dungeon)):
        if not visited[i] and dungeon[i][0] <= c_fatigue:
            visited[i] = True
            dfs(n + 1, c_fatigue - dungeon[i][1])
            visited[i] = False
