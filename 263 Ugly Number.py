"""263. Ugly Number https://leetcode.com/problems/ugly-number/ """

import time
from typing import List

class Solution:
    def isUgly(self, num: int) -> bool:
        n = num
        if n == 1:
            return True
        for i in [2, 3, 5]:
            while n and n != 1:
                if n % i != 0:
                    break
                else:
                    n = n // i
        return n == 1


        #

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().isUgly(8))
    print(Solution().isUgly(14))
    print(Solution().isUgly(4))
    print(Solution().isUgly(14))
    print(Solution().isUgly(20))
    print(Solution().isUgly(9))
    print(Solution().isUgly(13))
    print(Solution().isUgly(7))
    print(Solution().isUgly(8))
    print(Solution().isUgly(-8))
    print(Solution().isUgly(16))
    print(Solution().isUgly(-2147483648))
    print("--- %s seconds ---" % (time.time() - start_time))
