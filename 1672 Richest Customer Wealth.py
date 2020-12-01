"""1672. Richest Customer Wealth https://leetcode.com/problems/richest-customer-wealth/ """

import time
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(a) for a in accounts])


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().maximumWealth([[1,2,3],[3,2,1]]))
    print(Solution().maximumWealth([[1,5],[7,3],[3,5]]))
    print(Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

    print("--- %s seconds ---" % (time.time() - start_time))
