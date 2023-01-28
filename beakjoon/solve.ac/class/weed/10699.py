# 오늘 날짜
from datetime import *
print(datetime.now(tz=timezone(timedelta(hours=9))).strftime("%Y-%m-%d"))
