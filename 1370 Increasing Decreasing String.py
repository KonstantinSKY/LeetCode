"""1370 https://leetcode.com/problems/increasing-decreasing-string/"""

import time
from typing import List

class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        new = []
        rev = False
        while len(s) > 0:
            s1 = sorted(set(s), reverse=rev)
            new.extend(s1)
            for i in s1:
                s.remove(i)
            rev ^= 1
        return "".join(new)

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sortString("aaaabbbbcccc"))

    print("--- %s seconds ---" % (time.time() - start_time))
