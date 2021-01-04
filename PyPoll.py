# The data we need to retrieve 
# A complete list of candidates who received votes 
# The percentage of votes each candidate won
# The total number of votes each candidate won 
# The winner of the election based on popular vote.


#Add our dependencies:
import csv 
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the files to a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the files.
with open(file_to_load) as election_data:

    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Read and print the header row.
    headers = next(file_reader)
    print(headers)