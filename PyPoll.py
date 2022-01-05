#Add Dependencies
import csv
import os
#Assign Variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign Variable to save a file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#initialize total votes variable, candidate options list, and candidate votes dictionary
candidate_options = []
total_votes = 0
candidate_votes = {}
#Initialize winning_count, winning_percentage, and winning_candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open Election Results and Read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read Header Row
    header = next(file_reader)
    
    #Print Each Row in CSV file
    for row in file_reader:
        #print(row) (made as comment for ease of use for time being)
        #obtain total votes, add candidates to list, obtain votes per candidate
        total_votes += 1
        candidate_name = row[2]
    
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+= 1
#Saving Results to txt file
with open(file_to_save, "w") as txt_file:
    election_results = (
     f'\nElection Results\n'
     f'----------------------\n'
     f'Total Votes: {total_votes:,}\n'
     f'----------------------\n'   
    )
    print(election_results, end="")

    #Save the final vote count to the text file.
    txt_file.write(election_results)

    #Obtain percentage of voters per candidate
    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name]
        percentage_votes = float(votes) / float(total_votes) *100
        #print each candidates name, their votes, and their percentage of votes
        #print(f'{candidate_name}, {percentage_votes:.1f}%, ({votes:,})\n')
        
        #determine if the values are greater than the winning values, if true set winning values equal to values
        if (votes > winning_count) and (percentage_votes > winning_percentage):
            winning_count = votes  
            winning_percentage = percentage_votes
            winning_candidate = candidate_name
    
    #print winning candidate summary
    winning_summary = (
    f'-----------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-----------------\n')
    


#print the total_votes, candidate options, candidate votes, candidate percentage votes
#print(total_votes)
#print(candidate_options)    
#print(candidate_votes)
