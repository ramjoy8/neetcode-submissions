class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)



        res[0] = 1

        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]

        curr_right = 1
        for i in range(len(nums)-2,-1,-1):
            res[i] = res[i]*nums[i+1]*curr_right
            curr_right = nums[i+1]*curr_right

        return res