class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_rate = max(piles)


        left = 1

        right = max_rate
        res = max_rate

        while left <= right:

            mid = (left+right)//2

            hours = 0
            for each_pile in piles:
                hours += each_pile//mid

                remain = each_pile%mid

                if remain:
                    hours +=1
            if hours <= h:

                res = mid
                right = mid -1
            else:
                left = mid + 1

        return res
            




