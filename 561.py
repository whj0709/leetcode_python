# https://leetcode.com/problems/array-partition-i/description/
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list.sort(nums)
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

test = Solution()
assert test.arrayPairSum([1, 4, 3, 2]) == 4
