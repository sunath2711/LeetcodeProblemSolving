# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n <3:
            return False
        peak_index = arr.index(max(arr))
        if peak_index == 0 or peak_index == n-1:
            return False
        for i in range(0,peak_index):
            if arr[i+1] <= arr[i]:
                return False
        for i in range(peak_index,n-1):
            if arr[i+1] >= arr[i]:
                return False
        return True    

#find peak_index - for a while till peak all number be less and from peak to end all number be more, if not return false else return true
