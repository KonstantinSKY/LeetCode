import time
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(*strs)
        print(len(set('sfsdfds')))
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""

        first = strs[0]
        prefix = ""
        for i in range(1, len(first)+1):
            chk_prfx = first[:i]
            for j in range(len(strs)):
                if chk_prfx != strs[j][:i]:
                    return prefix
            prefix = chk_prfx
        return prefix

    def sds(self, strs: List[str]) -> str:
        result = ''
        if not strs:
            return ''
        else:
            print(set(zip(*strs)))
            for i in zip(*strs):
                print(i)
                print(set(i))
                if len(set(i)) == 1:
                    result += i[0]
                else:
                    break
        return result

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().sds(["flower", "flowe", "flowet"]))
    # print(Solution().longestCommonPrefix([]))
    # print(Solution().longestCommonPrefix(["a"]))
    # print(Solution().longestCommonPrefix(["asds"]))
    # print(Solution().longestCommonPrefix(["asds", ""]))

    print("--- %s seconds ---" % (time.time() - start_time))
