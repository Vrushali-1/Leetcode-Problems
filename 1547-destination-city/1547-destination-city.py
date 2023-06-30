class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = collections.Counter()
        for pair in paths:
            cities[pair[0]] += 1
            cities[pair[1]] += 0
        
        for city in cities:
            if cities[city] == 0:
                return city
        
        return ""
