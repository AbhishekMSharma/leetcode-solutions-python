class Solution:
    def canWinNim(self,n):
        if n%4!=0:
            return True
        else:
            return False

s=Solution()
print(s.canWinNim(4))