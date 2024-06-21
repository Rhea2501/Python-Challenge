import csv
import os


# Define the csv file path
# csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = os.path.join('PyBank\Resources','budget_data.csv')
# OR 
#csvpath = 'C:/Users/rheak/Documents/Bootcamp Assignment Resources/Starter_Code (3)/Starter_Code/PyBank/Resources/budget_data.csv'

# Define the output folder 
output_folder = 'PyBank\Analysis'
output_file = os.path.join(output_folder, 'financial_analysis.txt')


# Initialise variables
total_months = 0
net_total = 0
changes = []
dates = []
previous_profit_loss = None  # Initialising previous_profit_loss as None
average_change = 0
max_increase = 0
max_decrease = 0
max_increase_date = 0
max_decrease_date = 0


# Reading the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 

    # Process each row
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Count total months 
        total_months = total_months + 1
        
        #Sum of profit/losses
        net_total = net_total + profit_loss
        
        # Calculate changes
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        

        # Update previous profit/loss    
        previous_profit_loss = profit_loss      


# Calculate average change, greatest increase, and greatest decrease
if changes:   
    average_change = round(sum(changes) / len(changes), 2)
    max_increase = max(changes)
    max_decrease = min(changes)
    max_increase_date = dates[changes.index(max_increase)]
    max_decrease_date = dates[changes.index(max_decrease)]

else:
    average_change = 0
    max_increase = 0
    max_decrease = 0
    max_increase_date = ""
    max_decrease_date = ""
    

# Prepare the results
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
with open(output_file, 'w') as file:
    file.write(results)

print(f"Results have been written to {output_file}")