class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(str(s) for s in [(1-int(i)) for i in bin(num)[2:]]),2)

s = Solution()
print(s.findComplement(5))