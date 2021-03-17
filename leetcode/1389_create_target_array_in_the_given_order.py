from typing import List


class Solution:

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result


s = Solution()
print(s.createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
print(s.createTargetArray([1,2,3,4,0], [0,1,2,3,0]))