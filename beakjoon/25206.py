# 너의 평점은

import sys
input = sys.stdin.readline

score_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
s_score = 0.0
count_subject = 0
while v := input().split():
    subject, score, grade = v
    if grade == 'P':
        continue
    s_score += float(score) * score_dict[grade]
    count_subject += float(score)
print(f'{round(s_score/count_subject,6)}')
