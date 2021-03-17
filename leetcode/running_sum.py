from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        result = [nums[0]]

        for i in range(0, len(nums) - 1):
            last = result[i]
            num = nums[i + 1]
            result.append(last + num)

        return result


s = Solution()
print(s.runningSum([1,2,3,4]))
print(s.runningSum([3,1,2,10,1]))
print(s.runningSum([]))
