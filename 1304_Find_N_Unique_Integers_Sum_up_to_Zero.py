"""https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/ """

import time
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        num = [i+1 for i in range(n-1)]
        return [-sum(num), *num]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sumZero(14))

    print("--- %s seconds ---" % (time.time() - start_time))
