"""1636. Sort Array by Increasing Frequency https://leetcode.com/problems/sort-array-by-increasing-frequency/ """

import time
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums, reverse=True), key=nums.count)



if __name__ == "__main__":
    start_time = time.time()
    print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))
    print(Solution().frequencySort([2, 3, 1, 3, 2]))
    print(Solution().frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))

    print("--- %s seconds ---" % (time.time() - start_time))
