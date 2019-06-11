# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:55:17 2019

@author: guye0
"""

import os
import csv

# First step is initializing the vote summand, and candidate and vote vectors
totalvote = 0
candidate = []
votesper = []
percentper = []

# Set path for file

directory = os.path.dirname(os.path.realpath(__file__))

csvpath = os.path.join(directory,"election_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)  #skipping the header
    # We are now going to process these data for the final report
    for row in csvreader:
        totalvote = totalvote + 1
        if row[2] in candidate:
            seq = int(candidate.index(row[2]))
            votesper[seq] = votesper[seq] + 1
        else:
            candidate.append(row[2])
            votesper.append(1)
Winseq = votesper.index(max(votesper))
for i in range(len(votesper)):
    percentper.append("{:.3%}".format(votesper[i]/totalvote))

#Now we export the results to the console
print("Election Results")
print("---------------------------------------------")
print(f"Total Votes: {totalvote}")
print("---------------------------------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {percentper[i]} ({votesper[i]})")
print("---------------------------------------------")
print(f"Winner: {candidate[Winseq]}")
print("---------------------------------------------")

# Creating the simple little output file
output_file = os.path.join("output.txt")

# exporting the results to a text file
with open(output_file, "w") as writer:
    writer.write("Election Results\n")
    writer.write("---------------------------------------------\n")
    writer.write(f"Total Votes: {totalvote}\n")
    writer.write("---------------------------------------------\n")
    for i in range(len(candidate)):
        writer.write(f"{candidate[i]}: {percentper[i]} ({votesper[i]})\n")
    writer.write("---------------------------------------------\n")
    writer.write(f"Winner: {candidate[Winseq]}\n")
    writer.write("---------------------------------------------\n")