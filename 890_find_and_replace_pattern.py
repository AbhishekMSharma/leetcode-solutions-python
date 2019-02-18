'''
You have a list of words and a pattern, and you want to know which words in words matches the pattern.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
Return a list of the words in words that match the given pattern. 
You may return the answer in any order.
'''

class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: 'str') -> 'List[str]':
        pattern = self.getPattern(pattern)
        result = []
        for word in words:
            if self.getPattern(word) == pattern:
                result.append(word)
        return result
        
    def getPattern(self, s):
        value = 0
        visited_c = {}
        result = ""
        for c in s:
            if c in visited_c:
                result = result + str(visited_c[c])
            else:
                value += 1
                result = result + str(value)
                visited_c[c] = value
        return result
            
s = Solution()
print (s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")