from typing import List


class Solution:
    # [freq, val] = nums[2*i], nums[2*i+1], i >= 0
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        # iterate from 0 to nums size by 2
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i+1]
            # create new list by repeating [val] freq times and add to the result
            result.extend([val] * freq)
            # range(freq) is same as range(0, freq)
            #for j in range(freq):
            #    result.append(val)
        return result


s = Solution()
print(s.decompressRLElist([1, 2, 3, 4]))
print(s.decompressRLElist([1, 1, 2, 3]))
