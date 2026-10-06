class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_dict = {}

        for each_str in strs:

            count = [0]*26

            for each in each_str:

                count[ord(each)-ord('a')] +=1

            if group_dict.get(tuple(count)):
                group_dict.get(tuple(count)).append(each_str)

            else:
                group_dict[tuple(count)] = [each_str]

        return list(group_dict.values())

            