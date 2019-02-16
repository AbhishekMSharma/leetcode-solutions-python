# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

class Solution:
	def oneAway(self, s1, s2):
		if abs(len(s1) - len(s2)) > 1:
			return False
		elif len(s1) == len(s2):
			differenceCount = 0
			for i in range(len(s1)):
				if s1[i] != s2[i]:
					if differenceCount==1:
						return False
					differenceCount += 1
			return True
		else:
			if len(s1) > len(s2):
				return self.checkInsertRemove(s1, s2)
			else:
				return self.checkInsertRemove(s2, s1)
	
	def checkInsertRemove(self, s1, s2):
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				print ("In if", s1[i], s2[i])
				if s1[i+1:] == s2[i:]:
					return True
				else:
					return False
			
s = Solution()
print (s.oneAway('pale','bale'))
			
			