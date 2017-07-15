class Solution:
    def arrayPairSum(self,nums):
        nums.sort()
        sum = 0
        i = 0
        while i<len(nums):
            sum += min(nums[i], nums[i + 1])
            i+=2
        return sum

s = Solution()
print(s.arrayPairSum([1,4,2,3]))