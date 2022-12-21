# 시각
# 정수 n에대해서 00시 00분 00초 부터
# n시 59분 59초까지 3이하나라도 포함되는 모든 경우의 수를출력하시오

# 0~59까지 3이포함되는경우
# 30~39 = 10
import sys
n = int(sys.stdin.readline())


print((n+1)*60*60-len([x for x in range(n+1) if '3' not in str(x)]) *
      int('50', 9)*int('50', 9))  # => 3이포함되지않는 0~59의 갯수 // 45
