# Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.

class Solution:
	def isPermutationPalindrome(self, s):
		character_count = dict()
		odd_count = 0
		for c in s:
			if c in character_count:
				character_count[c] = character_count[c] + 1
				if character_count[c] %2 == 0:
					odd_count -= 1
				else:
					odd_count += 1
			else:
				character_count[c] = 1
				odd_count += 1
		if odd_count > 1: 
			return False
		else: 
			return True
		
s = Solution()
print(s.isPermutationPalindrome('zmralpzaryralarmp'))