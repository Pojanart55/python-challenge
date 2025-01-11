# -*- coding: UTF-8 -*-

# Import necessary modules
import csv  #import CSV module for reading CSV file
import os   #import OS module for interting with OS 

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources/election_data.csv")  # Input file path
file_to_output = os.path.join( "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_options =[] # Create a list to store unqiue candidate names
candidate_votes = {}  # Create a dictionary to store vote counts for each candidate

# Winning Candidate and Winning Count Tracker
winning_candidate = "" # Initiate an empty string to hold the winning candidate's name
winning_count = 0 #Initiate a variable to store the winning candidate's vote count

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2] # Candidate name is in the third column (index 2)

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
    
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------\n"
    )
    print(election_results)

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_options:
        votes = candidate_votes[candidate]
        votes_percentage = float(votes)/float(total_votes)*100

        # Get the vote count and calculate the percentage


        # Print and save each candidate's vote count and percentage
        voter_output = f"{candidate}: {votes_percentage: .3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
      

    # Generate and print the winning candidate summary
    winner_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------\n"
    )
    print(winner_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winner_summary)
