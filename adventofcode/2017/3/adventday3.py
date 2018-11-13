# Part 1

import math
from collections import defaultdict

input_num = 312051
# Find the next 'pivot'/'corner'. We know that all the lower right endpoints are odd squares,
# so we find the closest square to our input, rounding upwards.
ring = int(math.ceil(math.sqrt(input_num))) 
if ring % 2 == 0: # If square is even, make it odd.
    ring += 1
# The Manhattan Distance from one corner to the center is the 'size' of the ring currently - 1, since it's at a corner.
ring_manhattan_distance = ring - 1 
# We are travelling to the center of the ring, hence the division by two. Otherwise, we would travel to the other edge.
ring_manhattan_distance_one_axis = ring_manhattan_distance / 2 
# Find the distance from our nubmer to the pivot
distance_from_ring_pivot = ring**2 - input_num 
# Find the distance from our number to the center of one of the axes
along_ring_travel_distance = abs(ring_manhattan_distance_one_axis - distance_from_ring_pivot) 
# Our number has the advantage over a square in that we have, in a sense, travelled some of the distance already.
# Therefore, this could also be written as just the distance_from_ring_pivot, but hindsight is 20/20.
print along_ring_travel_distance + ring_manhattan_distance_one_axis 

# Part 2
numbers_checked = 1
current_x = 1
current_y = 0 # Let's treat our '1' at (0,0) as the origin, and start at (1,0)
value_to_alter = "x"
turns = 0
matrix = defaultdict(int)
matrix[(0,0)] = 1
max_value = 0
while max_value <= input_num:
    max_value = 0
    # Separated for readability.
    max_value = matrix[(current_x, current_y - 1)] + matrix[(current_x, current_y + 1)]
    max_value += matrix[(current_x - 1, current_y)] + matrix[(current_x + 1, current_y)]
    max_value += matrix[(current_x - 1, current_y - 1)] + matrix[(current_x - 1, current_y + 1)]
    max_value += matrix[(current_x + 1), (current_y + 1)] + matrix[(current_x + 1, current_y - 1)]
    #print matrix[(current_x, current_y)]
    if abs(current_x) == abs(current_y): # We've reached a corner.
        turns += 1
        if turns % 4 == 0:
            current_x += 1
            current_y -= 1
    pivot = turns % 4
    if pivot == 1:
        current_x -= 1
    if pivot == 2:
        current_y -= 1
    if pivot == 3:
        current_x += 1
    if pivot == 0:
        current_y += 1

print max_value

