# 크로아티아 알파벳
import sys
input = sys.stdin.readline

word = input().strip()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for c in cro:
    if c in word:
        word = word.replace(c, '0')
print(len(word))
