"""1662. Check If Two String Arrays are Equivalent https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/ """

import time
from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
    print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
    print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))


    print("--- %s seconds ---" % (time.time() - start_time))
