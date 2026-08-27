class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
        
        items=sorted(seen.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for item in items[:k]:
            result.append(item[0])

        return result