class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = { }
        final_list  = []
        count =0
        for i in nums:
            result[i] = result.get(i, 0) + 1 
        

        result = sorted(result.items(), key=lambda x : x[1], reverse = True)

        for k, v in result[:k]: 
            final_list.append(k)
        return final_list
