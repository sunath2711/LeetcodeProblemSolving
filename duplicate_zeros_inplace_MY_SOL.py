#Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] != 0:
                i+=1
                continue
            elif arr[i] == 0:
                for j in range(len(arr)-1,i+1,-1):
                    arr[j] = arr[j-1]
                arr[i+1] = 0
                i += 2
