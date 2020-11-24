"""922. Sort Array By Parity II  https://leetcode.com/problems/sort-array-by-parity-ii/ """

import time
from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        res = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        return res

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sortArrayByParityII([4,2,5,7]))

    print("--- %s seconds ---" % (time.time() - start_time))
