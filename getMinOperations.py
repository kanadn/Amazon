# def getMinOperations(weights, dist):
#     operations = 0
#     wzip = []
#     for i in range(len(weights)):
#         wzip.append([weights[i], i])
#     wzip.sort()
#     print(f"wzip: {wzip}")
#     movedpos = []
#     movedpos.append(wzip[0][1])
#     for i in range(1, len(wzip)):
#         while wzip[i][1] <= movedpos[-1]:
#             wzip[i][1] += dist[i]
#             operations += 1
#         print(f"movedpos: {movedpos}")
#         movedpos.append(wzip[i][1])
#     return operations

import math


def getMinOperations(weights, dists):
    n = len(weights)
    # Create a list of tuples: (weight, initial_position, move_distance)
    # Assuming positions are 1-indexed.
    points = [(weights[i], i + 1, dists[i]) for i in range(n)]
    
    # Sort points by their weights in ascending order
    points.sort(key=lambda x: x[0])
    
    total_moves = 0
    # The first point in sorted order can remain at its initial position
    prev_final_position = points[0][1]
    
    # Process each subsequent point
    for weight, pos, move_dist in points[1:]:
        if pos > prev_final_position:
            # No move needed if already to the right
            final_position = pos
            moves = 0
        else:
            # Calculate the minimum number of moves needed so that:
            # pos + moves * move_dist > prev_final_position
            moves = math.ceil((prev_final_position + 1 - pos) / move_dist)
            final_position = pos + moves * move_dist
        
        total_moves += moves
        prev_final_position = final_position
        
    return total_moves

print(getMinOperations([3,2,1], [1,4,5]))
print(getMinOperations([2,4,3,1], [2,6,3,5]))