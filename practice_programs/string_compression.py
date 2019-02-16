# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

class Solution:
	def stringCompression(self, s):
		compressed_string = ""
		current_char = s[0]
		current_count = 0
		for i in range(len(s)):
			if s[i] != current_char:
				compressed_string += current_char + str(current_count)
				current_count = 1
				current_char = s[i]
			else:
				current_count += 1
		compressed_string += current_char + str(current_count)
		return compressed_string if len(compressed_string) < len(s) else s
				
				
s = Solution()
print (s.stringCompression("aaaabbbbccd"))