class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        res = 0
        for each in set_nums:

            if not (each-1 in set_nums):
                curr = 1
                while each +1 in set_nums:
                    curr = curr +1
                    each = each + 1
                res = max(res,curr)

        return res