class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        ordered = sorted([[value,key] for key, value in counts.items()], reverse = True)
        answer = set()
        length = len(arr)
        
        for value, key in ordered:
            if length > len(arr)//2:
                length -= value
                answer.add(key)
            else:
                break
        return len(answer)
                
            
            