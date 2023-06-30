class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        coordinates = set()

        coordinates.add((x,y))

        for letter in path:
            if letter == 'N':
                y += 1
            elif letter == 'S':
                y -= 1
            elif letter == 'W':
                x -= 1
            else:
                x += 1
            
            if (x,y) in coordinates:
                return True
    
            coordinates.add((x,y))
            print(coordinates)
            
        return False
