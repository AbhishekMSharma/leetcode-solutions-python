class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list_next_greater_element = []
        for number in nums1:
            next_greater_element = -1
            for num in nums2[nums2.index(number)+1:]:
                if num > number:
                    next_greater_element = num
                    break
            list_next_greater_element.append(next_greater_element)
        return list_next_greater_element

s = Solution()
print (s.nextGreaterElement([2,4],[1,2,3,4]))
