import os 
import csv

# Get the directory of the currently running script (Main.py)
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the CSV file using the relative path from the script's directory
mypoll_csv = os.path.join(script_dir, 'Resources', 'election_data.csv')

print(" IIIIIIIIIIIII  This is the script's directory IIIIIIIIIIIIIII ")
print(script_dir)
print("%%%%%%%%%%%%% This is the file's location %%%%%%%%%%")
print(mypoll_csv)
print("*************** This is the Current Working Directory ****************")
print (os.getcwd())

# Path to save the analysis text file
output_txt = os.path.join(script_dir, 'Analysis', 'analysis.txt')
os.makedirs(os.path.dirname(output_txt), exist_ok=True)

# Check if the file exists and read it
if os.path.exists(mypoll_csv):
    print("File exists.")

    # Read the CSV file if it exists
    with open(mypoll_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        print(csvreader)

        csv_header = next(csvreader)
        print(f"CSV Header:")
        print(csv_header)

        total_votes = 0
        count_votes = 0
        
        candidates_and_votes = {}

        for row in csvreader:
            total_votes = total_votes + 1
            candidate = row[2]
            
            
            if candidate in candidates_and_votes:
                candidates_and_votes[candidate] = candidates_and_votes[candidate] + 1
            else:
                candidates_and_votes[candidate] = 1
                


    results = (
        f"\nELECTION RESULTS\n"
        f"--------------------------------------------------\n"
        f"TOTAL VOTES: {total_votes}\n"
        f"--------------------------------------------------\n"
    )


    percentage = 0

    for cand, votes in candidates_and_votes.items():
        percentage = (votes/total_votes)*100
        results += f"{cand} -> {votes} votes -> {round(percentage, 2)}%\n"

    
    winner = max(candidates_and_votes, key=candidates_and_votes.get)
    results += (
        f"--------------------------------------------------\n"
        f"The winner is {winner} with {candidates_and_votes[winner]} votes\n"
    )

    # Print the results to the terminal
    print(results)

    # Write the results to the text file
    with open(output_txt, 'w') as txtfile:
        txtfile.write(results)

    print(f"Results have been written to {output_txt}")

else:
    print("File does not exist.")


   
