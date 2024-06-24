class Solution:
    def numberOfPairs(self, nums1: [int], nums2: [int], k: int) -> int:
        n=len(nums1)
        m=len(nums2)
        count = 0
        for i in range(0,n):
            for j in range (0,m):
                if nums1[i]%(nums2[j]*k)==0 :
                    count += 1
        return count