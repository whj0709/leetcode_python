# https://leetcode.com/problems/hamming-distance/description/
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

test = Solution()
assert test.hammingDistance(1, 4) == 2
