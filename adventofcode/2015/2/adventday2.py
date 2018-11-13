f = open("adventday2text.txt")

papers = []

for line in f.readlines():
    papers.append(line)

# part 1
total_wrap = 0

for paper in papers:
    dims = map(int, paper.rstrip().split("x"))
    lw = dims[0] * dims[1]
    lh = dims[1] * dims[2]
    wh = dims[0] * dims[2]
    total_wrap += 2 * lw + 2 * lh + 2 * wh + min(lw, lh, wh)

print total_wrap

# part 2
total_ribbon = 0
for paper in papers:
    dims = map(int, paper.rstrip().split("x"))
    lw = 2 * (dims[0] + dims[1])
    lh = 2 * (dims[1] + dims[2])
    wh = 2 * (dims[0] + dims[2])
    total_ribbon += min(lw, lh, wh)
    total_ribbon += dims[0] * dims[1] * dims[2]

print total_ribbon
