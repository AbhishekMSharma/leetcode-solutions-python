import random

codes={}
url = "www.tinyurl.com/"
char_set = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Codec:

    def encode(self,s):
        count = 6
        code = ""
        while count:
            random_num = random.randint(0,len(char_set)-1)
            c = char_set[random_num:random_num+1]
            code += c
            count -= 1
        if code in codes:
            encode(self,s)
        else:
            codes[url+code] = s
            return url+code

    def decode(self,s):
        if s in codes:
            return codes[s]
        else:
            return "Not found"

codec = Codec()
decoded_string=codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(decoded_string)