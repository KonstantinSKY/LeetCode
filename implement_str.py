import time
from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().strStr("hello", "gg"))
    print(Solution().strStr("hello", "ll"))
    print(Solution().strStr("", ""))
    print(Solution().strStr("dof", "dofodfd"))

    print("--- %s seconds ---" % (time.time() - start_time))
