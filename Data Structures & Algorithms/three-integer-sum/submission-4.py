class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        i =0

        res = []

        while i < len(nums)-2:

            if i>0 and nums[i]==nums[i-1]:
                i = i+1
                continue 

            j = i+1
            k = len(nums) - 1

            while j < k:

                val = nums[i] + nums[j] + nums[k]

                if val < 0:
                    j = j + 1

                elif val > 0:

                    k = k -1

                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j = j+1
                    k = k-1

                    while j<k and nums[j-1] ==nums[j]:
                        j=j+1

                    while j<k and nums[k+1] ==nums[k]:
                        k=k-1
            i = i +1
        return res


