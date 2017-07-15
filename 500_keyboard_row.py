class Solution:
    def findWords(self,words):
        s1 = set("QWERTYUIOP")
        s2 = set("ASDFGHJKL")
        s3 = set("ZXCVBNM")
        result = []
        for word in words:
            if set(word.upper()).issubset(s1) or set(word.upper()).issubset(s2) or set(word.upper()).issubset(s3):
                result.append(word)
        return result


s = Solution()
res = s.findWords(["Hello", "Alaska", "Dad", "Peace"])
print(res)