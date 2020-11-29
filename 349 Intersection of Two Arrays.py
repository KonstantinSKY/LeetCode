"""349. Intersection of Two Arrays https://leetcode.com/problems/intersection-of-two-arrays/ """

import time
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().intersection([1,2,2,1], [2,2]))

    print("--- %s seconds ---" % (time.time() - start_time))
