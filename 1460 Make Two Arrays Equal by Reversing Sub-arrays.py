""" 1460. Make Two Arrays Equal by Reversing Sub-arrays https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/"""

import time
from typing import List


class Solution:
    def canBeEqual2(self, target: List[int], arr: List[int]) -> bool:
        return "".join(map(str, sorted(arr))) == "".join(map(str, sorted(target)))

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(arr) == sorted(target)

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
    print(Solution().canBeEqual([3, 7, 9], [3, 7, 11]))
    print("--- %s seconds ---" % (time.time() - start_time))
