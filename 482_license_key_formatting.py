class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-","").upper()[::-1]
        return '-'.join(S[i:i + K] for i in range(0, len(S), K))[::-1]

s = Solution()
print (s.licenseKeyFormatting("5F3Z-2e-9-w", 4))