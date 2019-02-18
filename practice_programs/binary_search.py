class Solution:
	def binarySearch(self, arr, n):
		while len(arr) >= 1:
			middle = int (len(arr) / 2)
			if n < arr[middle]:
				arr = arr[:middle]
			elif n > arr[middle]:
				arr = arr[middle+1:]
			else:
				return True
		return False
		
s = Solution()
print (s.binarySearch([0, 1, 4, 7, 10, 12, 18], 10))
print (s.binarySearch([0, 1, 4, 7, 10, 12, 18], 14))