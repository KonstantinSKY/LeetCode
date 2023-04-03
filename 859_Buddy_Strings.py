"""859. Buddy Strings https://leetcode.com/problems/buddy-strings/ """

import time
from typing import List


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == B and len(set(A)) < len(A):
            return True
        idx = []
        for i in range(len(A)):
            if A[i] != B[i]:
                idx.append(i)
            if len(idx) > 2:
                return False

        if len(idx) == 2 and A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]:
            return True

        return False


if __name__ == "__main__":
    start_time = time.time()

    print(Solution().buddyStrings("ab", "ba"))
    print(Solution().buddyStrings("ab", "bas"))
    print(Solution().buddyStrings("aa", "aa"))
    print(Solution().buddyStrings("ab", "ab"))
    print(Solution().buddyStrings("abcaa", "abcbb"))
    print("--- %s seconds ---" % (time.time() - start_time))
