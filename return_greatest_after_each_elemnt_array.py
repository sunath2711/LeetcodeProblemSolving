# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        if n == 1 or n == 0:
            return [-1]
        i = n -2
        greatest = arr[n-1]
        while i>0:
            if arr[i] >= greatest:
                greatest = arr[i]
            else:
                arr[i] = greatest
            i-=1
        arr.remove(arr[0])
        arr.append(-1)
        return arr
#main thing to remember is start array from back, array then take a temp as greatest in array if the next element is bigger than already greatest then
# replace the temp greatest with that value and move otherwise if smaller then assign that [i] the greatest value.
#just remove and append the first last element
  
