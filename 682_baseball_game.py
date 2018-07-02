class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        list_of_scores = []
        for operation in ops:
            try:
                list_of_scores.append(int(operation))
            except ValueError:
                if operation == '+': list_of_scores.append(sum(list_of_scores[-2:]))
                elif operation == 'D': list_of_scores.append(sum(list_of_scores[-1:]) * 2)
                elif operation == 'C': list_of_scores.pop()
        return sum(list_of_scores)

s = Solution()
print (s.calPoints(["5","2","C","D","+"]))
