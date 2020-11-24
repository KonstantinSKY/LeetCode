""" 557. Reverse Words in a String III https://leetcode.com/problems/reverse-words-in-a-string-iii/"""

import time
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])



if __name__ == "__main__":
    start_time = time.time()
    print(Solution().reverseWords("Let's take LeetCode contest"))

    print("--- %s seconds ---" % (time.time() - start_time))
