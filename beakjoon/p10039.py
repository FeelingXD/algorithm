#평균점수
def s_input():
    score =int(input())
    if score<40:
        score =40
    return score
s1=s_input()
s2=s_input()
s3=s_input()
s4=s_input()
s5=s_input()
print((s1+s2+s3+s4+s5)//5)
