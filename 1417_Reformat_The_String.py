"""1417. Reformat The String https://leetcode.com/problems/reformat-the-string/ """

import time
from typing import List

class Solution:
    def reformat(self, s: str) -> str:
        chars1 = list(filter(str.isalpha, s))
        chars2 = list(filter(str.isdigit, s))

        if abs(len(chars1) - len(chars2)) > 1:
            return ""

        if len(chars1) < len(chars2):
            chars1, chars2 = chars2, chars1

        return "".join([char for pair in zip(chars1, chars2) for char in pair] + chars1[len(chars2):])


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().reformat("a0b1c2d"))

    print("--- %s seconds ---" % (time.time() - start_time))
