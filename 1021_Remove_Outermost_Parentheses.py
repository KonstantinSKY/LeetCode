"""1021. Remove Outermost Parentheses https://leetcode.com/problems/remove-outermost-parentheses/ """

import time
from typing import List

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        s_ = []
        count = 0
        for i in S:
            if i == "(":
                count += 1
                if count != 1:
                    s_.append(i)
            else:
                count -= 1
                if count != 0:
                    s_.append(i)
        return "".join(s_)


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().removeOuterParentheses("(()())(())"))
    print(Solution().removeOuterParentheses("(()())(())(()(()))"))
    print(Solution().removeOuterParentheses("()()"))


    print("--- %s seconds ---" % (time.time() - start_time))
