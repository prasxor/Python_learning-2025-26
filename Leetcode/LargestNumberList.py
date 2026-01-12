class Solution:
    def largestElement(self, nums):
         nums.sort()
         return nums[-1]

arr = [1,2,3,65,22,86,2,5,-1,-353]

s1 = Solution()
print(s1.largestElement(arr))