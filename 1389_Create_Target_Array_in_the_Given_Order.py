""" https://leetcode.com/problems/create-target-array-in-the-given-order/"""

import time
from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1],))

    print("--- %s seconds ---" % (time.time() - start_time))
