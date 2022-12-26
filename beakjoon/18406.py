# 럭키 스트레이트
import sys
input = sys.stdin.readline
num = list(map(int, input().strip()))
print("LUCKY") if sum(num[:len(num)//2]
                      ) == sum(num[len(num)//2:]) else print("READY")
