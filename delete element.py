import time
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            if val in nums:
                nums.remove(val)
            else:
                return len(nums)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().removeElement([3,2,2,3], 3))


    print("--- %s seconds ---" % (time.time() - start_time))
