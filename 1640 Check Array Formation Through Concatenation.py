"""1640 https://leetcode.com/problems/check-array-formation-through-concatenation/ """

import time
from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            arr.

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().canFormArray([85],[[85]]))
    print(Solution().canFormArray([15,88], [[88],[15]]))


    print("--- %s seconds ---" % (time.time() - start_time))
