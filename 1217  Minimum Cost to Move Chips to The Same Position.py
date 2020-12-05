"""1217. Minimum Cost to Move Chips to The Same Position https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/ """

import time
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = odd = 0
        for pos in position:
            if pos % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().minCostToMoveChips([2, 2, 2, 3, 3]))
    print(Solution().minCostToMoveChips([1, 2, 3]))
    print("--- %s seconds ---" % (time.time() - start_time))
