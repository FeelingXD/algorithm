# 그룹 단어 체커
import sys
count = int(sys.stdin.readline())
answer = 0
for i in range(count):
    word = input()
    dic = {spell: -1 for spell in word}
    for index, spell in enumerate(word):
        if dic[spell] == -1:
            dic[spell] = index
        elif abs(dic[spell]-index) > 1:
            break
        dic[spell] = index
        if index == len(word)-1:
            answer += 1
print(answer, end='')
