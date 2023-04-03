""" 1668. Maximum Repeating Substring https://leetcode.com/problems/maximum-repeating-substring/"""

import time
from typing import List


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        while True:
            if word*(count+1) in sequence:
                count += 1
            else:
                return count


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().maxRepeating("ababc", "ab"))
    print(Solution().maxRepeating("aaa", "a"))

    print("--- %s seconds ---" % (time.time() - start_time))
