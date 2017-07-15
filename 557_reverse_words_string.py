class Solution:
    def reverseWords(self,s):
        word_list = s.split()
        s=""
        for word in word_list:
            s = s +" " + word[::-1]
        return s.strip()

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))