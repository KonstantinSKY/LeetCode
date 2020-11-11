""" """

import time
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = []
        for num in nums:
            count = 0
            for n in nums:
                if n < num:
                    count += 1
            new.append(count)
        return new

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))

    print("--- %s seconds ---" % (time.time() - start_time))
