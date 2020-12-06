"""1160. Find Words That Can Be Formed by Characters https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/ """

import time
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            for char in word:
                if char not in chars:
                    break
                

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().countCharacters(["cat","bt","hat","tree"], "atach"))

    print("--- %s seconds ---" % (time.time() - start_time))
