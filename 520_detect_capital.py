class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return True if max([ord(c) for c in word]) < 91 else False

s = Solution()
print (s.detectCapitalUse("g"))
