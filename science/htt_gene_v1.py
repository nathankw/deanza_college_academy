#!/usr/bin/env python

###
# Nathaniel Watson
# 2018-07-05
# De Anza College Academy
###

"""
In this exercise, you download the mRNA sequence for the htt gene - the gene associated with Huntington's Disease (http://hdsa.org/what-is-hd/).
The sequence can be downloaded from https://www.ncbi.nlm.nih.gov/nuccore/NM_002111.8?report=fasta by clicking on the "Send to" link, then
selectinng "File" in the "Choose Destination" section. Save the file to your thumddrive (D:). The file is automatically saved with the name
"sequence.fasta".

The htt gene resides on chromosome 4, and has a repeat of CAG in the DNA sequence. Normally, this repeats anywhere from 10 to 35 times. Repeats of 36 or more, however, result in
the disease. 

The in-class challenge was to download the mRNA sequence for the gene, then:
    1) Calculate the total sequence length,
    2) Count the number of times that G or C appears in the sequence and report this as a fraction of the total
       sequence length (a measure called GC content), and
    3) If you are up for the challenge, count how many CAG repeats are present in this gene sequence and then indicate whether or not
       this individual has the disease.
"""


import os
# Change directories to your D: drive:
os.chdir("D:")
fh = open("sequence.fasta", "r")
# The first line in the file is the sequence title. We don't need this for our program, though. 
title = fh.readline()
# The remaining lines are 
total = 0
g_total = 0
c_total = 0
for line in fh:
    line = line.strip()
    line = line.lower()
    line_length = len(line)
    total += line_length
    g_count = line.count("g")
    g_total += g_count
    c_count = line.count("c")
    c_total += c_count

print("Total G is: {}.".format(g_total))
print("Total C is: {}.".format(c_total))
print("GC content: {}.".format( (g_total + c_total)/total))
