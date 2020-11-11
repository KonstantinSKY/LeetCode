""" 1281 https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/"""

import time
from typing import List

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(i) for i in list(str(n))]
        res = 1
        for num in nums:
            res *= num
        return res - sum(nums)

    def subtractProductAndSum2(self, n: int) -> int:
        num_sum = 0
        num_mul = 1

        for c in str(n):
            num_sum += int(c)
            num_mul *= int(c)

        return num_mul - num_sum


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().subtractProductAndSum(234))

    print("--- %s seconds ---" % (time.time() - start_time))
