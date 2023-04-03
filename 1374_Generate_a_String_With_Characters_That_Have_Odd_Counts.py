"""1374 https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/"""

import time
from typing import List

class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return ["a"]
        if n % 2 == 0:
            return "".join(["a"] + ["b"] * (n-1))
        return "".join(["a", "b"] + ["c"] * (n-2))

class Solution:
    def generateTheString(self, n):
        if n % 2 ==0:
            return 'a' + 'b'* (n-1)
        return 'a' *n

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().generateTheString(4))
    print(Solution().generateTheString(1))
    print(Solution().generateTheString(7))
    print(Solution().generateTheString(22))

    print("--- %s seconds ---" % (time.time() - start_time))
