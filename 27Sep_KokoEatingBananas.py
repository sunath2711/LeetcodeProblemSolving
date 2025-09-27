class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)

        def checkHours(mid):
            hours = 0
            for i in range(len(piles)):
                if piles[i] <= mid:
                    hours+=1
                else:
                    hours = hours + (piles[i]//mid)
                    if piles[i]%mid != 0:
                        hours+=1
            return hours

        while right > left:
            mid = (left+right)//2
            hours_taken = checkHours(mid)
            if hours_taken > h:
                left = mid+1
            else:
                right = mid
        
        return left
        
