# https://leetcode.com/problems/unique-morse-code-words/description/
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_list = []
        for word in words:
            morse_str = ''
            for s in word:
                morse_str += morse_map[ord(s) - ord('a')]
            morse_list.append(morse_str)
        return len(set(morse_list))

test = Solution()
words = ["gin", "zen", "gig", "msg"]
assert test.uniqueMorseRepresentations(words) == 2
