class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = collections.Counter()
        zeroLoss = []
        oneLoss = []
        
        for match in matches:
            losers[match[1]] += 1
            losers[match[0]] += 0
        for loser in losers:
            if losers[loser] == 0:
                zeroLoss.append(loser)
            elif losers[loser] == 1:
                oneLoss.append(loser)
        
        
        return [sorted(zeroLoss),sorted(oneLoss)]