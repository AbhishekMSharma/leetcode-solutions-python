import math

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        loop_limit = len(B) + 1
        loop_start = math.ceil(len(B) / len(A))
        for count in range(loop_start, loop_limit):
            if B in A * count:
                return count
        return -1

s = Solution()
print("Solution",s.repeatedStringMatch("a","a"))