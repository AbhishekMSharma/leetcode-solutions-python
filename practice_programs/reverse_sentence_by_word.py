# The sky is blue
# blue is sky the
# with no extra space variable used

class Solution:
	def reverseSentenceByWord(self, s):
		p1 = p2 = len(s) - 1
		end = len(s)
		while p2 > 0:
			if s[p2] != ' ':
				p2 -= 1
			else:
				s += s[p2+1:p1+1] +" "
				p2 -= 1
				p1 = p2
		s += s[p2:p1+1]
		return s[end:]

s = Solution()
print (s.reverseSentenceByWord("the sky is blue"))
