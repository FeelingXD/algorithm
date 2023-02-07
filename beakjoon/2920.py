# 음계
import sys
input = sys.stdin.readline
codes = list(map(int, input().split()))

if codes == sorted(codes):
    print('ascending')
elif codes == sorted(codes, reverse=True):

    print('descending')
else:
    print('mixed')
