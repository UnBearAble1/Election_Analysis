# The data we need to retrieve
# 1. The total number of votes cast (done)
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Add our dependencies
import csv

import os

#Assign a variable to load a file from a path

file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

#Create Vote counter and set to 0
Total_votes = 0

#Create candidate list

candidate_options = []

#1. Declare the empty dictionary

candidate_votes = {}

#Winnning Candidate and Winningg Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object with the reader function

    file_reader  = csv.reader(election_data)

    #Read the header row

    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        
        Total_votes +=1

        # Get candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add it to the list of the candidates
            candidate_options.append(candidate_name)
            #2 Being tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidates count
        
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts

    #Iterate through the candidate list
            
    for candidate_name in candidate_options:

        #2 Retrieve vote count of a candidate

        votes = candidate_votes[candidate_name]
        
        #3 Calculate percetnage of votes

        vote_percentage = float(votes) / float(Total_votes) * 100

        #TO do: print out each candidtae's name, vote count and percentage of votes to the terminal
        
        #Determine winning vote count and candidate
        #Detemine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2 If true thwn set winning_count = votes and winning percent = Vote Percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3 Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

        print(f'{candidate_name}: {vote_percentage:.1f}%({votes:,})\n')
Winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")
print(Winning_candidate_summary)
