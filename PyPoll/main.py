import csv
import os

# Define the csv file path
# csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = os.path.join('PyPoll\Resources','election_data.csv')
# OR 
#csvpath = 'C:/Users/rheak/Documents/Bootcamp Assignment Resources/Starter_Code (3)/Starter_Code/PyBank/Resources/budget_data.csv'

# Define the output folder 
output_folder = 'PyPoll\Analysis'
output_file = os.path.join(output_folder, 'election_results.txt')


# OR Define the CSV file path
# csvpath = 'C:/Users/rheak/Documents/Bootcamp Assignment Resources/Starter_Code (3)/Starter_Code/PyPoll/Resources/election_data.csv'


# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0


# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print()


    # Process each row
    for row in csvreader:
        total_votes = total_votes + 1  # Count total votes explicitly
        candidate = row[2]  # Get the candidate's name
        
        # Count votes for each candidate explicitly
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

# Calculate percentage of votes and determine the winner
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results
print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print("Winner:", winner)
print("-------------------------")



with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------\n")
    for result in results:
        file.write(result + "\n")
    file.write("-------------------------\n")
    file.write("Winner: " + winner + "\n")
    file.write("-------------------------\n")

print("Results have been written to", output_file)
