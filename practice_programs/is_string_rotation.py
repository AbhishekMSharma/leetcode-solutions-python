# Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat").

class Solution:
	def isStrongRotation(self, s1, s2):
		if len(s1) != len(s2): return False
		if s2 in s1+s1: return True
		return False
		
s = Solution()
print (s.isStrongRotation('waterbottle', 'erbottlewat'))
