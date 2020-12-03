"""507. Perfect Number https://leetcode.com/problems/perfect-number/ """

import time
from typing import List

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        count = 1
        # for i in range(2, num):
        i = 1
        maxx = num - 1
        while i < maxx:
            if num % i == 0:
                maxx = num / i
                count += maxx
                count += i
                i += 1
                print (maxx)
        return count == num


if __name__ == "__main__":
    start_time = time.time()
    # print(Solution().checkPerfectNumber(99999991))
    print(Solution().checkPerfectNumber(28))
    print("--- %s seconds ---" % (time.time() - start_time))
