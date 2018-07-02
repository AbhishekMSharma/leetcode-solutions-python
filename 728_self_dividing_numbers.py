class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in range(left, right + 1) if '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))]

s = Solution()
print(s.selfDividingNumbers(1,22))
