class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        if l % 2 == 0:
            m = (nums1[l//2 - 1] + nums1[l//2]) / 2.0
        else:
            m = nums1[l//2]
        return m

s = Solution()

n = [1,3]
n1 = [2]
median = s.findMedianSortedArrays(n,n1)
print(median)

n = [1,2]
n1 = [3,4]
median = s.findMedianSortedArrays(n,n1)
print(median)
