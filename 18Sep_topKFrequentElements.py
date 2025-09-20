#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        sorted_dic = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [key for key, value in sorted_dic[:k]]


Appraocj -2 HEAP minheap

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        items = [(count,num) for num,count in freq.items()]
        heapq.heapify(items)

        top_k = heapq.nlargest(k, items, key=lambda x:x[0])
        return [num for count,num in top_k]


Appraoch - 3 Bucket Sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        arr = [[] for _ in range(n+1)]
        for key,value in freq.items():
            arr[value].append(key)

        res = []
        for i in range(n,0,-1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
            


        
