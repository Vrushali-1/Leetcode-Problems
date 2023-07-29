class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = sorted(zip(growTime,plantTime),reverse = True)
        current = 0
        maximum = 0
        for grow, plant in plants:
            current += plant
            maximum = max(maximum,current + grow)
        return maximum
