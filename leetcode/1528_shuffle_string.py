from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # create empty list of size same as string
        result = len(s) * [""]

        for i in range(0, len(indices)):
            char = s[i]
            index = indices[i]
            result[index] = char

        return "".join(result)


s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
print(s.restoreString("abc", [0,1,2]))
print(s.restoreString("aiohn", [3,1,4,2,0]))