
import argparse
import random

parser = argparse.ArgumentParser(description="howdy")
parser.add_argument("-i", "--infile", required=True, help="The input file containing names with one name per row.")
parser.add_argument("-o", "--outfile", required=True, help="The output file with random names selected repeatedly from the input file.")
args = parser.parse_args()
infile = args.infile
outfile = args.outfile

fh = open(infile)
fout = open(outfile, "w")
names = []
for line in fh:
    line = line.strip()
    names.append(line)

for i in range(1000):
    fout.write(random.choice(names))
    fout.write("\n")
fh.close()
fout.close()
