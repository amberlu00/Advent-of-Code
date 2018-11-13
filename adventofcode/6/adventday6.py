import copy
# (4074, 2793)

f = open("adventday6text.txt")

blocks = []
block = []
for entry in f.readline().split():
    block.append(int(entry))

while block not in blocks:
    blocks.append(block[:])
    max_num = max(block)
    max_index = block.index(max_num)
    i = block.index(max_num)
    block[max_index] = 0
    while max_num:
        i = (i + 1) % len(block)
        block[i] += 1
        max_num -= 1

print len(blocks)
print len(blocks) - blocks.index(block)
