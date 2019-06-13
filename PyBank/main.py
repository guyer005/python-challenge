# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:55:17 2019

@author: guye0
"""

import os
import csv

# First step is initializing the summand and min/max variables
months = 0
delta = 0
maxdelta = 0
mindelta = 0

# Set path for file
#directory = os.path.dirname(os.path.realpath(__file__))
#csvpath = os.path.join(directory,"budget_data.csv")
csvpath = os.path.join("budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)  #skipping the header
    # We are now going to process these data for the final report
    for row in csvreader:
        months = months + 1
        delta = delta + float(row[1])
        if float(row[1]) > maxdelta:
            maxdelta = float(row[1])
            maxrow = row
        if float(row[1]) < mindelta:
            mindelta = float(row[1])
            minrow = row
            
# Creating the simple little output
exports = []
exports.append("Financial Analysis")
exports.append("-----------------------------------------------------")
exports.append("Total Months: "+str(months))
exports.append("Total: $"+str(delta))
exports.append("Greatest Increase in Profits: "+maxrow[0]+" $"+maxrow[1])
exports.append("Greatest Decrease in Profits: "+minrow[0]+" $"+minrow[1])

print("\n".join(exports))

# save the output file path
output_file = os.path.join("output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as writer:
    longlist = "\n".join(exports)
    writer.writelines(longlist)

