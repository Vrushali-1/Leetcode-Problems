class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        maxheap = []
        answer = []

        for key, value in counts.items():
            heapq.heappush(maxheap,(-value, key))
            
        for _ in range(k):
            count,word = heapq.heappop(maxheap)
            answer.append(word)
        
        return answer

        
