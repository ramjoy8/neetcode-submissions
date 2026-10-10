class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq_map = {}

        for each in nums:
            freq_map[each] = freq_map.get(each,0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for each, count in freq_map.items():
            buckets[count].append(each)

        result = []

        for i in range(len(buckets)-1,0,-1):
            bucket = buckets[i]
            for each in bucket:
                if k==0:
                    return result
                else:
                    result.append(each)
                    k=k-1

        return result



        