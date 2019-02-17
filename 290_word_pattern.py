'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern: 'str', str: 'str') -> 'bool':
        words = str.split(" ")
        visited_words = set()
        if len(pattern) != len(words): return False
        map_d = dict()
        for i in range(len(pattern)):
            if pattern[i] not in map_d:
                if words[i] in visited_words:
                    return False
                map_d[pattern[i]] = words[i]
                visited_words.add(words[i])
            else:
                if map_d[pattern[i]] != words[i]:
                    return False
        return True
		
s = Solution()
print (s.wordPattern("abba", "dog cat cat fish"))
            