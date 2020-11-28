"""1399. Count Largest Group  https://leetcode.com/problems/count-largest-group/ """

import time
from typing import List

class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        nums = defaultdict(list)
        maxx = res = 0
        for i in range(1, n+1):
            r = i
            summ = 0
            while r > 0:
                summ += r % 10
                r //= 10
            nums[summ].append(i)
            length = len(nums[summ])
            if length == maxx:
                res += 1
            elif length > maxx:
                maxx = length
                res = 1
        return res


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().countLargestGroup(24))

    print("--- %s seconds ---" % (time.time() - start_time))
