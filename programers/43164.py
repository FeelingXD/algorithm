# 여행경로
def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, [])+[end]
    for r in routes.keys():
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]
