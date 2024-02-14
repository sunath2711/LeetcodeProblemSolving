class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        postive_nums = []
        negative_nums = []
        for i in nums:
            if i > 0:
                postive_nums.append(i)
            else:
                negative_nums.append(i)

        for i in range(len(postive_nums)):
            nums[2*i] = postive_nums[i]
            nums[(2*i)+1] = negative_nums[i]

        return nums



        
