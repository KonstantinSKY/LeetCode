"""1309H https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/ """

import time
from typing import List

class Solution:
    def freqAlphabets(self, s: str) -> str:
        new_arr = []
        i = len(s)-1
        while i >= 0:
            if s[i] == "#":
                new_arr.insert(0, chr(int(s[i-2:i])+96))
                i -= 3
            else:
                new_arr.insert(0, chr(int(s[i])+96))
                i -= 1
        return "".join(new_arr)




if __name__ == "__main__":
    start_time = time.time()
    print(Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))

    print("--- %s seconds ---" % (time.time() - start_time))
