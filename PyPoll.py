# Data needed
# 1) Total number of votes cast
# 2) Complete list of candidates who received votes
# 3) Total number of votes each candidate received
# 4) Percentage of votes each candidate won
# 5) Winner of the election based on popular vote

# Add dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Declare new list for candidate names
candidate_options = []
# Declare new dictionary for candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election reseults and read the file
with open(file_to_load) as election_data:

    # Read file object with reader function
    file_reader = csv.reader(election_data)

    # Get headers
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to total vote count
        total_votes += 1

        # Get candidate name from each row
        candidate_name = row[2]

        # Add name to candidate list if not already there
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Track candidates vote count
            candidate_votes[candidate_name] = 0

        # Add vote to candidates name
        candidate_votes[candidate_name] += 1

# Determine percentage of votes for each cnadidate by looping though the counts
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    #Calclate percentage of votes for candidate
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print out candidate names, vote counts, and vote percentages
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if votes are greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, set new winning count and winning percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set new winning candidate's name
        winning_candidate = candidate_name

# Print out winning candidate, vote count, and vote percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"-------------------------\n")

print(winning_candidate_summary)



