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

# Open election reseults and read the file
with open(file_to_load) as election_data:

    # Read file object with reader function
    file_reader = csv.reader(election_data)

    # Print headers
    headers = next(file_reader)
    print(headers)



