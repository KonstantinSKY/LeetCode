"""1502. Can Make Arithmetic Progression From Sequence https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/ """

import time
from typing import List


class Solution:
    def canMakeArithmeticProgression2(self, arr: List[int]) -> bool:
        arr.sort()
        delta = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != delta:
                return False
        return True

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta = arr[1] - arr[0]
        return all(arr[i] - arr[i - 1] == delta for i in range(2, len(arr)))



if __name__ == "__main__":
    start_time = time.time()
    print(Solution().canMakeArithmeticProgression([3, 5, 1]))
    print(Solution().canMakeArithmeticProgression([1, 2, 4]))
    print("--- %s seconds ---" % (time.time() - start_time))
