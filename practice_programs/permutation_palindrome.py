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
		print (character_count, odd_count)
		if odd_count > 1: 
			return False
		else: 
			return True
		
s = Solution()
print(s.isPermutationPalindrome('zmralpzaryralarmp'))