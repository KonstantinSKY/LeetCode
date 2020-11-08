import time
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass

    def firstlongestCommonPrefix(self, strs: List[str]) -> str:
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


    def fastest(self, strs: List[str]) -> str:
        result = ''
        if not strs:
            return ''
        else:
            print("list: ", strs)
            print("*list: ", *strs)
            print("zip(*strs): ", zip(*strs))
            print("list(zip(strs)): ", list(zip(strs)))
            print("list(zip(*strs)): ", list(zip(*strs)))
            print("set(zip(*strs): ", set(zip(*strs)))
            print("set(zip(*strs): ", set(zip(*strs)))
            print("set(zip(*strs[0]): ", set(zip(*strs)))

            for i in zip(*strs):
                print("i", i)
                print("set(i)", set(i))
                if len(set(i)) == 1:
                    result += i[0]
                else:
                    break
        return result

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().fastest(["flower", "flowesdf", "flowethj", "flyydfgr", "fluent"]))
    # print(Solution().longestCommonPrefix([]))
    # print(Solution().longestCommonPrefix(["a"]))
    # print(Solution().longestCommonPrefix(["asds"]))
    # print(Solution().longestCommonPrefix(["asds", ""]))

    print("--- %s seconds ---" % (time.time() - start_time))
