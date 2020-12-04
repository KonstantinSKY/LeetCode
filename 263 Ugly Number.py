"""263. Ugly Number https://leetcode.com/problems/ugly-number/ """

import time
from typing import List

class Solution:
    def isUgly(self, num: int) -> bool:



        
        Ans = []
        d = 2
        while d * d <= num:
            print(num)
            print("d", d)

            if num % d == 0:
                # Ans.append(d)
                # print (d)
                if d > 5:
                    return False
                else:
                    num //= d
            else:
                d += 1
        if num > 1:
            Ans.append(num)
        return True



        # factors = [2, 3, 5]
        # res = False
        # for factor in factors:
        #     if num % factor == 0:
        #         if num // factor not in factors:
        #             return False
        #         else:
        #             res = True
        # return res
        #

if __name__ == "__main__":
    start_time = time.time()
    # print(Solution().isUgly(8))
    print(Solution().isUgly(14))
    # # print(Solution().isUgly(4))
    # print(Solution().isUgly(14))
    # # print(Solution().isUgly(20))
    # # print(Solution().isUgly(9))
    # print(Solution().isUgly(13))
    # # print(Solution().isUgly(7))
    # print(Solution().isUgly(8))
    # print(Solution().isUgly(-8))
    # # print(Solution().isUgly(16))
    # # print(Solution().isUgly(-2147483648))
    print("--- %s seconds ---" % (time.time() - start_time))
