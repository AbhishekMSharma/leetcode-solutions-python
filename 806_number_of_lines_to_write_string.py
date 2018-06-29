class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        total = 0
        number_of_lines = 1
        for item in S:
            total += widths[ord(item) - 97]
            if total > 100:
                number_of_lines += 1
                total = widths[ord(item) - 97]
        return [number_of_lines, total]

s = Solution()
print (s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
