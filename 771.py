# https://leetcode.com/problems/jewels-and-stones/description/
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_set = set(J)
        jewel_list = list(jewel_set)
        jewel_list.sort()

        count = 0
        for s in S:
            for j in jewel_list:
                if s == j:
                    count += 1
        
        return count

test = Solution()
assert test.numJewelsInStones("aA", "aAAbbbb")==3
assert test.numJewelsInStones("z", "ZZ")==0
