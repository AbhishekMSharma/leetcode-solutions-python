class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_indexes = [i for i,c in enumerate(S) if c==C]
        shortest_distances = []
        for i in range(len(S)):
            shortest_distances.append(min([abs(i-j) for j in c_indexes]))
        return shortest_distances

s = Solution()
print(s.shortestToChar("loveleetcode","e"))