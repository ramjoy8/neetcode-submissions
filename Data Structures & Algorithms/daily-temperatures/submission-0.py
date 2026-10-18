class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        result = [0]*len(temperatures)
        tmp = []


        for i in range(len(temperatures)):

            while tmp and temperatures[i] > temperatures[tmp[-1]]:
                last = tmp.pop()
                dur = i - last 
                result[last] = dur

            tmp.append(i)

        return result
