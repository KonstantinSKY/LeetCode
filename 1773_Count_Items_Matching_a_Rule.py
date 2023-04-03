class Solution:

    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        rule_keys = {'type': 0, 'color': 1, 'name': 2}
        res = 0
        for item in items:
            res += 1 if item[rule_keys[ruleKey]] == ruleValue else 0
        return res


if __name__ == "__main__":
    Solution().countMatches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                            "type", "phone")
