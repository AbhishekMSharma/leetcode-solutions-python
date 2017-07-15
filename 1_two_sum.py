class Solution:
    def twoSum(self,numbers,target):
        if len(numbers) <=1:
            return False
        dict_num = {}
        for i in range(len(numbers)):
            if numbers[i] in dict_num:
                return [dict_num[numbers[i]],i]
            else:
                dict_num[target-numbers[i]]=i

sum_object = Solution()
n = [8,-3,4]
t = 6
list_num = sum_object.twoSum(n,t)
print(list_num)