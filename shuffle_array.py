""" https://leetcode.com/problems/shuffle-the-array/"""

import time
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(int(len(nums) / 2), 0, -1):
            nums.insert(i, nums.pop(-1))
        return nums


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))
    print(Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
    print(Solution().shuffle([1, 1, 2, 2], 2))

    print("--- %s seconds ---" % (time.time() - start_time))
