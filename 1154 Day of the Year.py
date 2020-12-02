"""1154. Day of the Year https://leetcode.com/problems/day-of-the-year/ """

import time
from typing import List

class Solution:
    def dayOfYear(self, date: str) -> int:
        import datetime
        return int(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%j'))

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().dayOfYear("2019-01-09"))

    print("--- %s seconds ---" % (time.time() - start_time))
