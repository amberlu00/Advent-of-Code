f = open("adventday5text.txt")
jump_list_p1 = []
jump_list_p2 = []

for line in f.readlines():
	jump_list_p1.append(int(line))
	jump_list_p2.append(int(line))

# Part 1
current_placement = 0
steps = 0
while current_placement < len(jump_list_p1):
	jump_list_p1[current_placement] += 1
	current_placement += (jump_list_p1[current_placement] - 1)
	steps += 1
print steps

# Part 2
current_placement = 0
steps = 0
while current_placement < len(jump_list_p2):
	if jump_list_p2[current_placement] >= 3:
		jump_list_p2[current_placement] -= 1
		current_placement += (jump_list_p2[current_placement] + 1)
	else:
		jump_list_p2[current_placement] += 1
		current_placement += (jump_list_p2[current_placement] - 1)
	steps += 1
	#print current_placement
print steps