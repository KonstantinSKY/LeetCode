""" https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/"""

import time
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [candie + extraCandies >= max_candies for candie in candies]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
    print(Solution().kidsWithCandies([12, 1, 12], 10))
    print(Solution().kidsWithCandies([1], 10))

    print("--- %s seconds ---" % (time.time() - start_time))
