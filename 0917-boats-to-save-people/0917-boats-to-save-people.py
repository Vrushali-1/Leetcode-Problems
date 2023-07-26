class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,answer,j = 0,0,len(people) - 1
        people.sort()
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1 
            j -= 1
            answer += 1
        return answer