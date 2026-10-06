class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = dict()

        for i,each in enumerate(nums):
            need = target - each
            if seen.get(need) is not None:
                return [seen.get(need),i]
            else:
                seen[each] = i

        return []