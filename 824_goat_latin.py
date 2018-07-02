class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        return " ".join([word+"ma"+"a"*(i+1)  if word[0].upper() in ['A','E','I','O','U'] else word[1:]+word[0]+"ma"+"a"*(i+1) for i, word in enumerate(S.split(" "))])

s = Solution()
print (s.toGoatLatin("I speak Goat Latin"))
