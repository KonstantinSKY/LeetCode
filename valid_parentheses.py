import time
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        last_open = []
        coll = {"]": "[", ")": "(", "}": "{"}
        for char in s:
            if char in coll.values():
                last_open.append(char)
                continue
            if not last_open or last_open[-1] != coll[char]:
                return False
            last_open.pop()
        if last_open:
            return False
        return True


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().isValid("(){}"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("{[]}"))

    print("--- %s seconds ---" % (time.time() - start_time))

