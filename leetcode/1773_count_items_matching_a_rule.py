from typing import List


class Solution:
    # items[i] = type, color, name
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0
        for e_type, color, name in items:
            if (ruleKey == "color" and color == ruleValue) or \
                    (ruleKey == "type" and e_type == ruleValue) or \
                    (ruleKey == "name" and name == ruleValue):
                counter += 1

        return counter


s = Solution()
print(
    s.countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color",
                   "silver"))
print(s.countMatches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type",
                     "phone"))
