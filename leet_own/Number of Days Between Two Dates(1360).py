import calendar
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1=date1.split("-")
        d2=date2.split("-")
        da1=calendar.datetime.date(int(d1[0]),int(d1[1]),int(d1[2]))
        da2=calendar.datetime.date(int(d2[0]),int(d2[1]),int(d2[2]))
        return  abs((da2-da1).days)
print(Solution().daysBetweenDates("2020-01-15","2019-12-31"))
#-----------------------------------------------------------------------------
import calendar
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def get_days(date):
            y, m, d = map(int, date.split('-'))
            return calendar.timegm((y, m, d, 0, 0, 0))
        return abs(get_days(date1) - get_days(date2)) // (24 * 60 * 60)
print(Solution().daysBetweenDates("2020-01-15","2019-12-31"))
#-----------------------------------------------------------------------------
import calendar
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((datetime.strptime(date1, '%Y-%m-%d') - datetime.strptime(date2, '%Y-%m-%d')).days)
print(Solution().daysBetweenDates("2020-01-15","2019-12-31"))

