f = open("adventday6text.txt")
blocks = []
correct_total = 0
for entry in f.readline().split():
	blocks.append(int(entry))
	correct_total += int(entry)
correct_total /= len(blocks)

while b in blocks != correct_total:
	print True