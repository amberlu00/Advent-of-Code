import re

# Quick reference:
# index 0: target register
# index 1: dec/inc
# index 2: number to dec/inc by
# index 3: "if", ignored
# index 4: confirmation register
# index 5: operator
# index 6: number

f = open("adventday8text.txt")

instructions = []
for entry in f.readlines():
    instructions.append(entry.rstrip())

# part 1
register = dict()
operator = {"<=": (lambda x, y: x <= y),
            "<": (lambda x, y: x < y),
            ">=": (lambda x, y: x >= y),
            ">": (lambda x, y: x > y),
            "==": (lambda x, y: x == y),
            "!=": (lambda x, y: x != y)}

dec_inc = {"dec": (lambda x, y: x - y),
          "inc": (lambda x, y: x + y)}

# variable for part 2
highest = 0

for i in instructions:
    register[re.findall("[a-zA-Z]+", i)[0]] = 0

for i in instructions:
    order = i.split()
    if operator[order[5]](register[order[4]], int(order[6])):
        register[order[0]] = dec_inc[order[1]](register[order[0]], int(order[2]))
        if register[order[0]] > highest:
            highest = register[order[0]]

print register[max(register, key=register.get)]
print highest



