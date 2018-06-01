#Part 1
total_sum = 0
for line in open("adventday2text.txt"):
	min_num = "inf"
	max_num = 0
	for num in line.split():
		if int(num) < min_num:
			min_num = int(num)
		if int(num) > max_num:
			max_num = int(num)
	total_sum += (max_num - min_num)

#Part 2
total_sum = 0
for line in open("adventday2text.txt"):
	num_array = []
	for num in line.split():
		num_array.append(int(num))
	for num_1 in num_array:
		for num_2 in num_array:
			if num_1 % num_2 == 0 and num_1 != num_2:
				total_sum += (num_1 / num_2)


print total_sum