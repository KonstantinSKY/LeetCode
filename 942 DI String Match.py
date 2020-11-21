""" 942 https://leetcode.com/problems/di-string-match/"""

import time
from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:

        lenx = len(S)
        lx = {"I": 0, "D": -1}
        arr = [i for i in range(lenx+1)]
        res = [arr.pop(lx[S[0]])]
        for i in range(1, lenx):
            res.append(arr.pop(lx[S[i]]))
        return res + arr


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().diStringMatch("IDID"))
    print(Solution().diStringMatch("III"))
    print(Solution().diStringMatch("DDI"))

    print("--- %s seconds ---" % (time.time() - start_time))
