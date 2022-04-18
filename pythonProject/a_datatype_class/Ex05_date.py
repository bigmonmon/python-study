"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""

from datetime import date
today = date.today()
print('today is ', today)
print('today is ', today.year)
print('today is ', today.month)
print('today is ', today.day)

from datetime import datetime, timedelta
today = datetime.today()
print('today is ', today.hour)

print('-'*50)
print('todat +10 is ', today + timedelta(days=10))
print('todat -10 is ', today + timedelta(days=-10))

#오늘 날짜에서 3개월 후
print('-'*50)
#print('todat +3m is ', today + timedelta(months=10)) => 에러발생
#python-dateutil 패키지를 추가 설치 필요
from dateutil.relativedelta import relativedelta
print(today + relativedelta(months=3))
