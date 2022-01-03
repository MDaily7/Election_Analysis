#Add Dependencies
import csv
import os
#Assign Variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign Variable to save a file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#Open Election Results and Read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read and Print Header Row
    header = next(file_reader)
    print(header)
    