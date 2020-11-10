""" https://leetcode.com/problems/merge-sorted-array/"""

import time
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[0:n]
        nums1.sort()
        print(nums1)


if __name__ == "__main__":
    start_time = time.time()
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 2)
    Solution().merge([1, 2, 3, 0, 0, 0], 4, [2, 5, 6], 3)
    Solution().merge([1, 2, 3, 0, 0, 0], 2, [2, 5, 6], 2)

    print("--- %s seconds ---" % (time.time() - start_time))
