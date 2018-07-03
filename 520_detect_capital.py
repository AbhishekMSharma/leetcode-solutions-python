class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1: return True
        if word.upper() == word: return True
        if word.lower() == word: return True
        if 64 < ord(word[0]) < 91 and all(96 < ord(c) < 123 for c in word[1:]): return True
        return False

s = Solution()
print (s.detectCapitalUse("flag"))
