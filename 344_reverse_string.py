class Solution():
    def reverseString(self,s):
        reversed_string = ""
        length = len(s)-1
        while length>=0:
            reversed_string+=s[length]
            length-=1
        return reversed_string


s = Solution()
print(s.reverseString(("Hello")))