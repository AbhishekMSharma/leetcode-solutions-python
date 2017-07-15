class Solution:
    def distributeCandies(self,candies):
        unique_list = list(set(candies))
        print(unique_list)
        dict_count={}
        i=0
        c1=c2=[]
        for item in unique_list:
            dict_count[item]=candies.count(item)
        print(dict_count)
        while i<len(dict_count):
            if dict_count[unique_list[i]]%2==0:
                c1+=unique_list[i]/2
                c2+=unique_list[i]/2
            else:
                if i%2==0:
                    c1+=1
                else:
                    c2+=1
            i+=1
        return max(c1,c2)

s = Solution()
print(s.distributeCandies([1000,1,1,1]))