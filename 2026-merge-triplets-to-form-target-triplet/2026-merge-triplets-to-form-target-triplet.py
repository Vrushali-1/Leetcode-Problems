class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        good = [0 for _ in range(3)]

        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            
            for j in range(3):
                if target[j] == triplets[i][j]:
                    good[j] = triplets[i][j]
        return good == target