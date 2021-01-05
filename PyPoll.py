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

#1 initialize a voter count 
total_votes = 0 

#Candidate Option
candidate_options = []

#1 Declare the empty dictionary.
candidate_votes = {}

#winning candidate and winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    #print each row in the CSV file.
    for row in file_reader:
        #add to the total vote count. 
        total_votes += 1

        #print the candidate name from each row.
        candidate_name = row[2]

        #IF candidate does not match any existing candiate
        if candidate_name not in candidate_options:
            #Add it to the list of candidates 
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's vote counnt. 
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1 

#Determine the percentage of votes for each candidate by looping through the counts. 
#1. Iterate through the candidate list. 
for candidate_name in candidate_votes:

    #2 retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. calculate the percentage of votes. 
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. Print the candidate name and percentage of total votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_count):
        #If true then set the winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #And set the winning_candidate equal to the candidate's name. 
        winning_candidate = candidate_name

        winning_candidate_summary = ( f"-------------------------\n" f"Winner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage: {winning_percentage:.1f}%\n" f"-------------------------\n")
        print(winning_candidate_summary)
    
