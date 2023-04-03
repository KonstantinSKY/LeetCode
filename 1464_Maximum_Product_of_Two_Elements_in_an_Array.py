"""1454 https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/"""

import time
from typing import List


class Solution:
    def maxProduct2(self, nums: List[int]) -> int:
        elem_1 = max(nums)
        nums.remove(elem_1)
        return (elem_1 - 1) * (max(nums) - 1)

    def maxProduct(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        return (arr[0] - 1) * (arr[1] - 1)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().maxProduct([1, 5, 4, 5]))

    print("--- %s seconds ---" % (time.time() - start_time))
