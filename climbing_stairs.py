""" https://leetcode.com/problems/climbing-stairs/"""

import time
from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        return 2*n-2 if n > 3 else n

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(4))
    print(Solution().climbStairs(5))
    print(Solution().climbStairs(1))
    print(Solution().climbStairs(6))
    print("--- %s seconds ---" % (time.time() - start_time))

