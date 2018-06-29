class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1-number for number in inner_list [::-1]] for inner_list in A]

s = Solution()
print (s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
