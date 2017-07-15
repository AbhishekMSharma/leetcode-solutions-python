class Solution:
    def hammingDistance(self,x,y):
        dist = 0
        x = format(x,"0256b")
        y = format(y,"0256b")
        x_length = len(x) - x.find("1")
        y_length = len(y) - y.find("1")
        if x_length > y_length:
            x = x[-x_length:]
            y = y[-x_length:]
        else:
            x = x[-y_length:]
            y = y[-y_length:]
        for i in range(len(x)):
            if x[i]!=y[i]:
                dist += 1
        return dist



s = Solution()
a = s.hammingDistance(1,5)
print(a)