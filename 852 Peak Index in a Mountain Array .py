"""852. Peak Index in a Mountain Array https://leetcode.com/problems/peak-index-in-a-mountain-array/ """

import time
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))

    print("--- %s seconds ---" % (time.time() - start_time))
