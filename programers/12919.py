#김서방 찾기
def solution(seoul):
    for index,name in enumerate(seoul):
        if name =="Kim":
            return f'김서방은 {index}에 있다'