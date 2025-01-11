# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "Resources/budget_data.csv"  # Input file path
file_to_output = os.path.join("analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0  # Initialize a counter for the total number of months  
total_net = 0  # Initialize a variable to store the total net profit/loss

# Add more variables to track other necessary financial data
net_changes_list = [] # Create an empty list to store the net changes in profit/loss
previous_profit_loss = 0  # Initialize a variable to store the profit/loss from the previous month
greatest_increase = ["",0] # Initialize a list to store the date and amount of greatest increase
greatest_decrease = ["",99999999999999999] # Initialize a list to store the date and amount of the greatest decrease

# Open and read the csv
print(file_to_load)
with open(file_to_load) as financial_data:  #Open the input file in read mode
    reader = csv.reader(financial_data, delimiter=",") # Create a CSV reader object

    # Skip the header row
    header = next(reader)  # Read and discard header row

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)        # Read the first row of data
    total_months += 1               # Increment the total months counter
    total_net += int(first_row[1])  # Add the profit/loss data (index 1) from the first row to the total
    previous_profit_loss = int(first_row[1]) # Store the profit/loss from the first row

    # Track the total of months and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1 # Increment the total months counter
        total_net += int(row[1]) #Add the profit/loss from the current row to the total

        # Track the net change
        net_change = int(row[1]) - previous_profit_loss # Calculate the net change
        net_changes_list.append(net_change)  # Append the net change to the list
        previous_profit_loss = int(row[1])   # Update previouse profit/loss for the next iteration

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]: # Check if the current net change is greater than the previouse greatest increase
            greatest_increase[0] = row[0]     # Update the date of the greatest increase
            greatest_increase[1] = net_change # Update the amount of the greatest increase

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]: # Check if the current net change is less than the previous greatest decrease
            greatest_decrease[0] = row[0]     # Update the date of the greatest decrease
            greatest_decrease[1] = net_change # Update the amount of the greatest decrease
    
# Calculate the average net change across the months
average_change = sum(net_changes_list)/ len(net_changes_list)  # Calcuate the average of the net changes

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Changes: ${round(average_change,2)}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]}  (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

# Print the output
print(output) # Print the analysis results

# Write the results to a text file
with open(file_to_output, "w") as txt_file: 
    txt_file.write(output)