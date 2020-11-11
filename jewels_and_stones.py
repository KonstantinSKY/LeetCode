"""https://leetcode.com/problems/jewels-and-stones/ """

import time
from typing import List


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().numJewelsInStones("aA", "aAAbbbb"))

    print("--- %s seconds ---" % (time.time() - start_time))
