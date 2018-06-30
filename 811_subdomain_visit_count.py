class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        subdomain_dict = {}
        for item in cpdomains:
            count = int(item.split(" ")[0])
            reversed_domain = item.split(" ")[1][::-1]
            dot_index = [i for i,c in enumerate(reversed_domain) if c=='.'] + [len(reversed_domain)]
            values = []
            for i in dot_index:
                values.append(reversed_domain[:i][::-1])
            for value in values:
                if value in subdomain_dict:
                    subdomain_dict[value] = subdomain_dict[value] + count
                else:
                    subdomain_dict[value] = count;
        subdomain_count = []
        for key, value in subdomain_dict.items():
            subdomain_count.append(str(value) + " " + key)
        return subdomain_count

s = Solution()
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))