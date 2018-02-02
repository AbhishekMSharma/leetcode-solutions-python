class Solution:
    def numJewelsInStones(self, J, S):
        sum = 0
        for item in J:
            sum = sum + S.count(item)
        return sum




