f = open("adventday1text.txt")
num = f.read()
num_size = len(num)

# Part 1
sum = 0
for x in range(num_size - 1):
	if int(num[x]) == int(num[x+1]):
		sum += int(num[x])
if int(num[0]) == int(num[num_size - 1]):
	sum += int(num[0])

print sum

# Part 2
sum = 0
half_size = num_size / 2
for x in range(num_size - 1):
	if int(num[x]) == int(num[(x + half_size) % num_size]):
		sum += int(num[x])

print sum