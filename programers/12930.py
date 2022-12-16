#이상한문자만들기
def solution(s):
    s= s.upper()
    answer=[]
    for word in list(s.split(' ')):
        temp_word=''
        for index,spell in enumerate(word):
            if index%2==1:
                temp_word+=spell.lower()
            else:
                temp_word+=spell
        answer.append(temp_word)
            
    return ' '.join(answer)