""" 905 https://leetcode.com/problems/sort-array-by-parity/ """

import time
from typing import List


class Solution:
    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        res = []
        for num in A:
            if num % 2 == 0:
                res.insert(0, num)
            else:
                res.append(num)
        return res

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res1 = []
        res2 = []
        for num in A:
            if num & 1 == 0:
                res1.append(num)
            else:
                res2.append(num)
        return res1 + res2


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sortArrayByParity([3, 1, 2, 4]))

    print("--- %s seconds ---" % (time.time() - start_time))
