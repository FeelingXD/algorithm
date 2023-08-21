# AC
import sys
from collections import deque
input = sys.stdin.readline

case = int(input())

# R 뒤집기 D 버리기

for _ in range(case):
    reverse_check = False
    error_check = False
    cmd = input().rstrip()
    l = int(input())
    li = list(input().rstrip()[1:-1].split(","))
    q = deque(list(filter(None, li)))
    for c in cmd:
        match c:
            case "R":
                reverse_check = False if reverse_check else True
                pass
            case "D":
                if q:
                    if reverse_check:
                        q.pop()
                    else:
                        q.popleft()
                else:
                    error_check = True
                    print("error")
                    break
                pass
    if not error_check:
        print(
            f'[{",".join(q)}]' if not reverse_check else f'[{",".join(reversed(q))}]')
