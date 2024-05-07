import math

# Function to find orientation of three points (p, q, r)
# Returns the following values:
# 0 : Collinear points
# 1 : Clockwise points
# 2 : Counterclockwise points
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise

# Function to perform Graham's scan algorithm
def convex_hull(points):
    # Number of points
    n = len(points)
    
    # If there are less than 3 points, convex hull is not possible
    if n < 3:
        return None
    
    # Find the point with the smallest y-coordinate. This point is always on the convex hull.
    start = min(points, key=lambda point: (point[1], point[0]))
    
    # Sort the remaining points by their polar angle with respect to the starting point.
    def polar_angle(point):
        return math.atan2(point[1] - start[1], point[0] - start[0])
    
    sorted_points = sorted(points, key=polar_angle)
    
    # Initialize the stack to store the convex hull
    stack = [start, sorted_points[0]]
    
    # Iterate through the remaining points
    for i in range(1, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])
    
    return stack

# Example usage:
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_points = convex_hull(points)
print("Convex Hull Points:")
for point in convex_points:
    print(point)
