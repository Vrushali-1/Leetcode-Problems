class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        def binarySearchLeft(time,target):
            left, right = 0, len(time)

            while left < right:
                mid = (left + right) // 2
                if time[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        def binarySearchRight(time,target):
            left, right = 0, len(time)
            while left < right:
                mid = (left + right) // 2
                if time[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        start, end, answer = [], [], []

        for flower in flowers:
            start.append(flower[0])
            end.append(flower[1])
        
        start.sort()
        end.sort()

        for t in people:
            answer.append(binarySearchRight(start,t)-binarySearchLeft(end,t))
        
        return answer