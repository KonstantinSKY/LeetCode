
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_list = []
        while x > 0:
            num_list.append(x % 10)
            x //= 10
        while len(num_list) > 1:
            if num_list.pop(0) != num_list.pop(-1):
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(1))
