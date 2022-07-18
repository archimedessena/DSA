# You are given an array coordinates, coordinates[i] = [x, y], 
# where [x, y] represents the coordinate of a point. Check if these points make a 
# straight line in the XY plane.
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true


def checkStraightLine(self, coordinates) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
                print(coordinates)
                if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                        return False
        return True
    
    
  
    
    
# def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#         (x0, y0), (x1, y1) = coordinates[: 2]
#         return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)