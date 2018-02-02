class Solution:
    def judgeCircle(self, moves):
        """
        :param moves:
        :return: bool
        """
        return moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R")