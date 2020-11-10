"""https://leetcode.com/problems/plus-one/"""

import time
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().plusOne([1,2,3]))
    print(Solution().plusOne([4,3,2,1]))
    print(Solution().plusOne([9]))
    print(Solution().plusOne([9, 9 ]))

    print("--- %s seconds ---" % (time.time() - start_time))
