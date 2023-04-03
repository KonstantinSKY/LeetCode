"""1046. Last Stone Weight https://leetcode.com/problems/last-stone-weight/ """

import time
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort(reverse=True)
            if stones[0] != stones[1]:
                stones.append(abs(stones[0] - stones[1]))
            stones.pop(0)
            stones.pop(0)
        return stones[0] if len(stones) == 1 else 0


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
    print(Solution().lastStoneWeight([2, 2]))
    print("--- %s seconds ---" % (time.time() - start_time))
