"""7 https://leetcode.com/problems/reverse-integer/"""


class Solution:
    def reverse(self, x: int) -> int:
        res = lambda x_: int("".join(list(str(x_))[::-1]))
        res = res(x) if x >= 0 else -res(-x)
        return res if -2**31 <= res <= 2**31 else 0


if __name__ == "__main__":
    print(Solution().reverse(-199994))


