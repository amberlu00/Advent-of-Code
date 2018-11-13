f = open("adventday1text.txt")

long_string = f.read()

# part 1

open_count = long_string.count("(")
close_count = long_string.count(")")

print open_count - close_count


# part 2
index = 1
floor = 0
for p in long_string:
    if p == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break
    index += 1

print index

