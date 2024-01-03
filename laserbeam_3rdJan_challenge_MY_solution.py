# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

# There is one laser beam between any two security devices if both conditions are met:

# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.

#Problem socha sahi bas implement faster krna tha


class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        sum_list = [sum(map(int, binary_string)) for binary_string in bank]
        total = 0
        i =0 
        while i < len(sum_list) - 1:
            if sum_list[i]!=0 and sum_list[i+1]!=0:
                total += sum_list[i] * sum_list[i+1]
                i = i+1
            elif sum_list[i]==0 and sum_list[i+1]==0:
                i = i+2
            elif sum_list[i]!=0 and sum_list[i+1]==0:
                j=i+1
                while sum_list[j]==0:
                    j += 1
                total += sum_list[i] * sum_list[j]
                i = j
        return total   
