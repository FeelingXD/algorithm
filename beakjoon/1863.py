import sys
input = sys.stdin.readline

case = int(input())
cnt = 0
stack = []
for _ in range(case):
    x, y = map(int, input().split())

    # 새로 입력받은 건물 y가 작을경우 기존의 높은건물들의 갯수를 새줌
    while len(stack) > 0 and stack[-1] > y:
        cnt += 1
        stack.pop()
    if len(stack) > 0 and stack[-1] == y:  # 새로들어오는 건물y가 기존과 같을경우
        continue

    stack.append(y)

while len(stack) > 0:  # 스택에 값이 남아있을경우 + 높이가 0이 아닌경우 건물
    if stack[-1] > 0:
        cnt += 1
    stack.pop()

print(cnt)
