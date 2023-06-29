class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        answer = float('inf')
        seen = collections.Counter()
        left = 0
        for right in range(len(cards)):
            seen[cards[right]] += 1
            if seen[cards[right]] > 1 :
                while seen[cards[right]] > 1:
                    answer = min(answer,right - left + 1)
                    seen[cards[left]] -= 1
                    if seen[cards[left]] == 0:
                        del seen[cards[left]]
                    left += 1
        return answer if answer != float('inf') else -1
