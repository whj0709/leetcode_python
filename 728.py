# https://leetcode.com/problems/self-dividing-numbers/description/
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numbers = []

        for i in range(left, right + 1):
            divide = set(str(i))
            for j in divide:
                flag = False
                number = int(j)
                if number == 0:
                    break
                
                if i % number != 0:
                    break

                flag = True
            
            if flag:
                numbers.append(i)
 
        return numbers


test = Solution()
print(test.selfDividingNumbers(1, 22))
