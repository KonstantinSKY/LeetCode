"""https://leetcode.com/problems/length-of-last-word/"""
import time
from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        return len(s_list[-1]) if s_list else 0


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("Hello World f"))
    print(Solution().lengthOfLastWord("Hello"))
    print(Solution().lengthOfLastWord(""))
    print(Solution().lengthOfLastWord(" "))
    print(Solution().lengthOfLastWord("      "))
    print("--- %s seconds ---" % (time.time() - start_time))
