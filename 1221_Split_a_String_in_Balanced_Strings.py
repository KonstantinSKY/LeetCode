"""1221 https://leetcode.com/problems/split-a-string-in-balanced-strings/ """

import time
from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = r = 0
        for i in s:
            l += 1 if i == 'R' else -1
            r += 1 if l == 0 else 0
        return r

    def balancedStringSplit2(self, s: str) -> int:
        l = r = 0
        for i in s:
            l += 1 if i == 'R' else 0
            l -= 1 if i == 'L' else 0
            r += 1 if l == 0 else 0
        return r


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().balancedStringSplit('RLRRLLRLRL'))
    print(Solution().balancedStringSplit('RLLLLRRRLR'))
    print(Solution().balancedStringSplit('LLLRRRR'))
    print(Solution().balancedStringSplit('RLRRRLLRLL'))

    print("--- %s seconds ---" % (time.time() - start_time))
