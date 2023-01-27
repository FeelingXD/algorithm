# 달팽이는 올라가고 싶다
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())  # 올라가는 거리, 자는동안 떨어지는거리 ,목표

print(1 if V-A <= 0 else (V-A)//(A-B) +
      1 if ((V-A) % (A-B)) == 0 else (V-A)//(A-B)+2)
