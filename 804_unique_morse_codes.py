class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        return len({''.join(morse_codes[ord(letter) - 97] for letter in word) for word in words})


s  = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg", "fiv"]))
