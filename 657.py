# https://leetcode.com/problems/judge-route-circle/description/
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        import collections
        counter = (collections.Counter(moves))
        return counter['U'] == counter['D'] and counter['L'] == counter['R']

test = Solution()
assert test.judgeCircle("UD") == True
assert test.judgeCircle('LL') == False
