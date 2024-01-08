# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sett = set()
        for num in arr:
            if num*2 in sett or (num%2 == 0 and num//2 in sett) or (num % 2 == 1 and num * 2 in sett):
                return True
            sett.add(num)
        return False
#use set concept here
#if new element then add to set and check for 2n and n//2 if present reture true otherwise false
  
