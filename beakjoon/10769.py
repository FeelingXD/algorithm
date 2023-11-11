#행복한지 슬픈지
import sys
input=sys.stdin.readline
HAPPY=":-)"
SAD=":-("
if __name__ =="__main__":
    text=input().strip()
    c_happy=text.count(HAPPY)
    c_sad=text.count(SAD)
    if c_happy == c_sad ==0:
        print("none")
    else:
        if c_happy==c_sad:
            print("unsure")
        else:
            print("happy") if c_happy>c_sad else print("sad")    
    pass