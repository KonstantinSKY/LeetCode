import time
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1, 3, 5, 6], 0))
    print(Solution().searchInsert([1], 0))
    print(Solution().searchInsert([1], 1))

    print("--- %s seconds ---" % (time.time() - start_time))
