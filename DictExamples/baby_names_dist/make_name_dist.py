

import os

os.chdir("D:")

f = open("dist_1000_baby_girl_names.txt.txt", "r")

d = {}

for line in f:
    line = line.strip()
    if line in d:
        d[line] += 1
    else:
        d[line] = 1

max_freq = 0
max_name = ""
for name in d:
    freq = d[name]
    if freq > max_freq:
        max_freq = freq
        max_name = name

