class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_dict = {}
        for i in range(len(accounts)):
            current_position = i
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in email_dict:
                    current_position = email_dict[accounts[i][j]]
                    for k in range(1, len(accounts[i])):
                        email_dict[accounts[i][k]] = current_position
                    j = 0
                else:
                    email_dict[accounts[i][j]] = current_position
        filtered_dict = {}
        for key, value in email_dict.items():
            if value in filtered_dict:
                temp = filtered_dict[value] + [key]
                temp.sort()
                filtered_dict[value] = temp
            else:
                filtered_dict[value] = [key]
        output_list = []
        for key, value in filtered_dict.items():
            output_list += [[accounts[key][0]] + value]
        return output_list



s = Solution()
print(s.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com", "ja@mail.com"], ["John", "johnnybravo@mail.com","j@mail.com", "j@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com", "j@mail.com"], ["Mary", "mary@mail.com"]]))
