"""922. Sort Array By Parity II  https://leetcode.com/problems/sort-array-by-parity-ii/ """

import time
from typing import List

class Solution:
    def sortArrayByParityII2(self, A: List[int]) -> List[int]:
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

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        odd, even = 1, 0
        for a in A:
            if a % 2:
                res[odd] = a
                odd += 2
            else:
                res[even] = a
                even += 2

        return res

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sortArrayByParityII([4,2,5,7]))

    print("--- %s seconds ---" % (time.time() - start_time))
