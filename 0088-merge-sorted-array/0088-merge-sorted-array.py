class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        for j in range(n):
          nums1[m+j] = nums2[j]
        nums1.sort()
        print(nums1)
    
                
s = Solution()        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1,m,nums2,n)

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
s.merge(nums1,m,nums2,n)

        