""" 905 https://leetcode.com/problems/sort-array-by-parity/ """

import time
from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res = []
        for num in A:
            if num % 2 == 0:
                res.insert(0, num)
            else:
                res.append(num)
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sortArrayByParity([3,1,2,4]))

    print("--- %s seconds ---" % (time.time() - start_time))
