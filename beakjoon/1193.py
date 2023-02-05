# 분수찾기
import sys
input = sys.stdin.readline

num = int(input())
line = 0  # 줄
end = 0  # 줄의 끝지점
while num > end:
    line += 1
    end += line
diff = end-num
if line % 2 == 1:
    top = diff+1
    bottom = line-diff
else:
    top = line-diff
    bottom = diff+1
print(f'{top}/{bottom}')
