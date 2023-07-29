class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        start = 1
        moves = 0

        while target > 1 and maxDoubles > 0:
            moves += 1 + (target % 2)
            target //= 2
            maxDoubles -= 1
        return moves + target - 1