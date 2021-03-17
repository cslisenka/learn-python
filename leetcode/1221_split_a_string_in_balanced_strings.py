class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # counts of L and R characters
        l_count, r_count = 0, 0

        # moving until we reach end of the string
        result = 0
        for i in range(len(s)):
            # if we found a sub-string with same number of L and R
            if l_count == r_count and l_count > 0:
                result += 1
                l_count, r_count = 0, 0

            if s[i] == "L":
                l_count += 1
            if s[i] == "R":
                r_count += 1

        return result + 1


s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
print(s.balancedStringSplit("RLLLLRRRLR"))