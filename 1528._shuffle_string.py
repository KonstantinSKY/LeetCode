"""1528 https://leetcode.com/problems/shuffle-string/ """

import time
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new = [None] * len(s)
        for i, index in enumerate(indices):
            new[index] = s[i]
        return "".join(new)

    def restoreString2(self, s: str, indices: List[int]) -> str:
        temp = {indices[i]: s[i] for i in range(len(s))}
        return "".join([temp[i] for i in range(len(temp))])


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))

    print("--- %s seconds ---" % (time.time() - start_time))