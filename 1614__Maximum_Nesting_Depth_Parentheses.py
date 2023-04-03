"""https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/ """

import time
from typing import List

class Solution:
    def maxDepth(self, s: str) -> int:
        max_d = d = 0
        for i in s:
            if i == '(':
                d += 1
                if d > max_d:
                    max_d = d
            elif i == ')':
                d -= 1
        return max_d


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().maxDepth('(1+(2*3)+((8)/4))+1)'))

    print("--- %s seconds ---" % (time.time() - start_time))
