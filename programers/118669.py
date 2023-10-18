# 등산코스 정하기
import heapq


def solution(n, paths, gates, summits):
    '''
    n 노드
    paths 엣지
    gates 시작가능지
    summits 봉우리

    @return [산봉우리번호 ,intensity의 최솟값] 가능한 산봉우리번호는 작도록 반환
    '''

    inf = float('inf')
    graph = [[] for _ in range(n+1)]

    # 그래프 그리기
    for s, e, w in paths:
        graph[s].append((e, w))
        graph[e].append((s, w))

    # 봉우리 판별
    is_summit = [0]*(n+1)

    for summit in summits:
        is_summit[summit] = 1

    # 시작위치
    distance = [inf]*(n+1)
    q = []

    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q, (0, gate))  # (intend, 번호 저장)

    while q:
        d, i = heapq.heappop(q)  # inten 과 현재index
        if distance[i] < d or is_summit[i]:
            continue
        for t, w in graph[i]:
            new_intensity = max(d, w)
            if new_intensity < distance[t]:
                distance[t] = new_intensity
                heapq.heappush(q, (new_intensity, t))

    answer = [-1, inf]

    for summit in sorted(summits):
        if distance[summit] < answer[1]:
            answer = [summit, distance[summit]]
    print(distance)
    print(answer)
    return answer


solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4],
         [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
