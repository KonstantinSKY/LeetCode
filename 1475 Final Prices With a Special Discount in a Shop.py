"""1475 https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/ """

import time
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)-1):
            for j in prices[i+1:]:
                if prices[i] >= j:
                    prices[i] -= j
                    break
        return prices


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().finalPrices([8, 4, 6, 2, 3]))
    print(Solution().finalPrices([1, 2, 3, 4, 5]))

    print("--- %s seconds ---" % (time.time() - start_time))
