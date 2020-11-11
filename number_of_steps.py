"""https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/ """

import time
from typing import List


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            num = num / 2 if int(num % 2) == 0 else num - 1
            steps += 1
        return steps


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().numberOfSteps(123))

    print("--- %s seconds ---" % (time.time() - start_time))
