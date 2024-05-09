import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise
    
def convex_hull(points):
    n = len(points)
    
    if n < 3: # If there are less than 3 points, convex hull is not possible
        return None
    
    start = min(points, key=lambda point: (point[1], point[0])) # calculating the point with min y-coordinate, if tie then min x-coordinate.This point is always on the convex hull.
    
    def polar_angle(point):
        return math.atan2(point[1] - start[1], point[0] - start[0])
    
    sorted_points = sorted(points, key=polar_angle) # custom sort function to sort points according to thier polar angle wrt starting point
    
    stack = [start, sorted_points[0]] # we need atleast 2 points to determine the relative position of 3rd element(if it's counter clockwise or not)

    for i in range(1, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])
    
    return stack

# points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
points = [(1, 1), (2, 4), (3, 2), (4, 0), (5, 1), (5, 5), (6, 3),(7,1)]
convex_points = convex_hull(points)
print("Convex Hull Points:")
for point in convex_points:
    print(point)