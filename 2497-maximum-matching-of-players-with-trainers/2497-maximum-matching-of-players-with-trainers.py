class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse = True)
        trainers.sort(reverse = True)

        i,j, matching = 0, 0, 0
       
        while i<len(players) and j<len(trainers):
            if players[i] <= trainers[j]:
                matching += 1
                j += 1
            i += 1
        return matching
            