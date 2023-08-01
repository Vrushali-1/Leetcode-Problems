class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(minSweet):
            currentSweetness = 0
            people = 0
            for sweet in sweetness:
                currentSweetness += sweet

                if currentSweetness >= minSweet:
                    people += 1
                    currentSweetness = 0
            return people >= k + 1
        
        left, right = min(sweetness), sum(sweetness) // (k + 1)

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left


        