import os

os.chdir("D:")
f = open("colors.txt", "r")

d = {}
for color in f:
    color = color.strip()
    if color in d:
        d[color] += 1
    else:
        d[color] = 1

max_freq = 0
max_freq_col = ""
for color in d:
    freq = d[color]
    if freq > max_freq:
        max_freq = freq
        max_freq_col = color

        
