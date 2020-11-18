"""728 https://leetcode.com/problems/self-dividing-numbers/ """

import time
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            j = i
            while j > 0:
                digit = j % 10
                if digit == 0 or i % digit != 0:
                    break
                j //= 10
            if j == 0:
                res.append(i)
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().selfDividingNumbers(1, 22))

    print("--- %s seconds ---" % (time.time() - start_time))
