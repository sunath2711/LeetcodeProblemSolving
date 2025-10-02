class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Ensure nums1 is smaller in size than nums2
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1

        m,n = len(nums1), len(nums2)

        total = m+n
        half = (total+1)//2
        #half is for partitioning of left size

        l,r = 0,m
        while l<=r:
            i = (l+r)//2
            j = half - i

            # left and right boundaries
            left1 = nums1[i-1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j-1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # check if partition is correct
            if left1 <= right2 and left2 <= right1:
                # odd total length
                if total % 2 == 1:
                    return max(left1, left2)
                # even total length
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1




        
