class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(int(len(candies) / 2), len(set(candies)))
        
s = Solution()
print(s.distributeCandies([1,1,2,2,3,3]))
